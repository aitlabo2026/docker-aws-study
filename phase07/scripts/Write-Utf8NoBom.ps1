function Write-Utf8NoBom {
    param(
        [Parameter(Mandatory)]
        [string]$Path,

        [Parameter(Mandatory)]
        [string]$Value
    )

    $normalized = $Value.Replace("`r`n", "`n")
    $normalized = $normalized.Replace("`r", "`n")
    $normalized = $normalized.Replace("`t", "    ")
    $normalized = [regex]::Replace($normalized, '\p{Zs}', ' ')
    $normalized = [regex]::Replace($normalized, '[\u200B\uFEFF]', '')

    $target = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Path)
    $encoding = New-Object System.Text.UTF8Encoding($false)

    [IO.File]::WriteAllText($target, $normalized, $encoding)
}