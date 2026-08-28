function Write-CheckedUtf8 {



    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)][string]$LiteralPath,
        [Parameter(Mandatory=$true,ValueFromPipeline=$true)][AllowEmptyString()][string]$Text
    )
    begin { $parts = New-Object 'System.Collections.Generic.List[string]' }
    process { $parts.Add($Text) }
    end {
        $value = ($parts -join "`n").Replace("`r`n", "`n").Replace("`r", "`n")
        $pattern = '[^\S\r\n ]|\p{Cf}|[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]'
        $bad = [regex]::Match($value, $pattern)
        if ($bad.Success) {
            $prefix = $value.Substring(0, $bad.Index)
            $line = ([regex]::Matches($prefix, "\n")).Count + 1
            $column = $bad.Index - $prefix.LastIndexOf("`n")
            throw ('Special whitespace/control character: {0}, line {1}, column {2}, U+{3:X4}; file not written.' -f $LiteralPath,$line,$column,[int][char]$bad.Value[0])
        }
        $target = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($LiteralPath)
        $encoding = New-Object System.Text.UTF8Encoding($false)
        [IO.File]::WriteAllText($target, $value, $encoding)
        $bytes = [IO.File]::ReadAllBytes($target)
        if ($bytes.Length -ge 3 -and $bytes[0] -eq 239 -and $bytes[1] -eq 187 -and $bytes[2] -eq 191) {
            throw 'Unexpected UTF-8 BOM.'
        }
    }



}