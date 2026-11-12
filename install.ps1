# Registers the consult-to-build pipeline with Claude Code by copying files (this computer only).
# To use it everywhere and keep it synced, install the plugin instead: see README.md.
#   .\install.ps1                      - installs the 18 agents globally
#   .\install.ps1 -Project C:\path\to  - also sets up a project with commands,
#                                        guardrails, hook and log compiler
param([string]$Project)

$ErrorActionPreference = "Stop"
$src    = $PSScriptRoot
$claude = Join-Path $env:USERPROFILE ".claude"
$fresh  = -not (Test-Path $claude)

# --- global: the agents ---------------------------------------------------
$agentDir = Join-Path $claude "agents"
New-Item -ItemType Directory -Force -Path $agentDir | Out-Null
Copy-Item (Join-Path $src "agents\*.md") $agentDir -Force
$n = (Get-ChildItem $agentDir -Filter *.md).Count
Write-Host "Installed $n agents to $agentDir" -ForegroundColor Green

if ($fresh) {
  Write-Host ""
  Write-Host "NOTE: $claude did not exist before now." -ForegroundColor Yellow
  Write-Host "That usually means Claude Code has not run on this machine yet." -ForegroundColor Yellow
  Write-Host "Install it and run 'claude' once, then restart it so the new" -ForegroundColor Yellow
  Write-Host "agents directory is picked up." -ForegroundColor Yellow
}

# --- per project ----------------------------------------------------------
if ($Project) {
  if (-not (Test-Path $Project)) { throw "Project path not found: $Project" }

  New-Item -ItemType Directory -Force -Path `
    (Join-Path $Project ".claude\commands"), `
    (Join-Path $Project "hooks"), `
    (Join-Path $Project "scripts") | Out-Null

  Copy-Item (Join-Path $src "commands\*.md")            (Join-Path $Project ".claude\commands") -Force
  Copy-Item (Join-Path $src "templates\CLAUDE.md")       $Project -Force
  Copy-Item (Join-Path $src "templates\AGENTS.md")       $Project -Force
  Copy-Item (Join-Path $src "hooks\block_signed_writes.py") (Join-Path $Project "hooks") -Force
  Copy-Item (Join-Path $src "scripts\log_compile.py")    (Join-Path $Project "scripts") -Force

  $settings = Join-Path $Project ".claude\settings.json"
  if (Test-Path $settings) {
    Write-Host "settings.json already exists - merge the hook by hand from dot-claude\settings.json" -ForegroundColor Yellow
  } else {
    Copy-Item (Join-Path $src "dot-claude\settings.json") $settings -Force
    Write-Host "Installed the G2 signed-file hook" -ForegroundColor Green
  }
  Write-Host "Project set up at $Project" -ForegroundColor Green
}

Write-Host ""
Write-Host "Next: restart Claude Code, then run /context to confirm what loaded."
