function Write-Utf8NoBom {
    param(
        [string]$Path,
        [string]$Value
    )

    $normalized = $Value.Replace("`r`n", "`n").Replace("`r", "`n").Replace("`t", "    ")
    $normalized = [regex]::Replace($normalized, '[\p{Zs}-[ ]]', ' ')
    $normalized = [regex]::Replace($normalized, '[\u200B\uFEFF]', '')

    $target = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Path)
    $encoding = New-Object System.Text.UTF8Encoding($false)
    [IO.File]::WriteAllText($target, $normalized, $encoding)
}