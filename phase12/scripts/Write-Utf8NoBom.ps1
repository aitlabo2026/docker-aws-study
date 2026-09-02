function Write-Utf8NoBom {
    param(
        [Parameter(Mandatory = $true)]
        [string]$LiteralPath,

        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string]$Text
    )

    $Text = $Text.Replace([string][char]0xFEFF, '')
    $Text = $Text.Replace([string][char]0x200B, '')

    $specialSpaceCodes = @(
        0x00A0,
        0x1680,
        0x180E,
        0x2000,
        0x2001,
        0x2002,
        0x2003,
        0x2004,
        0x2005,
        0x2006,
        0x2007,
        0x2008,
        0x2009,
        0x200A,
        0x202F,
        0x205F,
        0x3000
    )

    foreach ($specialSpaceCode in $specialSpaceCodes) {
        $specialSpace = [string][char]$specialSpaceCode
        $Text = $Text.Replace($specialSpace, ' ')
    }

    foreach ($character in $Text.ToCharArray()) {
        $characterCode = [int]$character

        if (
            $characterCode -lt 32 -and
            $characterCode -notin @(9, 10, 13)
        ) {
            throw "Unsupported control character in: $LiteralPath"
        }
    }

    $outputPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($LiteralPath)
    $parentDirectory = [IO.Path]::GetDirectoryName($outputPath)

    if (
        -not [string]::IsNullOrWhiteSpace($parentDirectory) -and
        -not (Test-Path -LiteralPath $parentDirectory -PathType Container)
    ) {
        New-Item `
            -Path $parentDirectory `
            -ItemType Directory `
            -Force |
            Out-Null
    }

    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [IO.File]::WriteAllText($outputPath, $Text, $utf8NoBom)
}