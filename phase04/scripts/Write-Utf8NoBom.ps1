function Write-Utf8NoBom {
    param([Parameter(Mandatory=$true)][string]$LiteralPath,[Parameter(Mandatory=$true)][string]$Value)
    $fullPath = [System.IO.Path]::GetFullPath($LiteralPath)
    $encoding = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($fullPath, $Value, $encoding)
}