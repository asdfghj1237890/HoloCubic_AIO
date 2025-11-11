# Setup script for CubicAIO_Tool
# This script automates the installation of dependencies

Write-Host "=== CubicAIO_Tool Setup ===" -ForegroundColor Cyan
Write-Host ""

# Check if uv is installed
Write-Host "Checking for uv..." -ForegroundColor Yellow
try {
    $uvVersion = uv --version
    Write-Host "[OK] $uvVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] uv is not installed!" -ForegroundColor Red
    Write-Host "Please install uv from: https://github.com/astral-sh/uv" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Step 1: Creating virtual environment..." -ForegroundColor Yellow
uv venv
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to create virtual environment" -ForegroundColor Red
    exit 1
}
Write-Host "[OK] Virtual environment created" -ForegroundColor Green

Write-Host ""
Write-Host "Step 2: Installing all dependencies (including esptool)..." -ForegroundColor Yellow
uv pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to install dependencies" -ForegroundColor Red
    exit 1
}
Write-Host "[OK] All dependencies installed" -ForegroundColor Green

Write-Host ""
Write-Host "=== Setup Complete ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "You can now run the application with:" -ForegroundColor Yellow
Write-Host "  uv run python CubicAIO_Tool.py" -ForegroundColor White
Write-Host ""
Write-Host "Or build the executable with:" -ForegroundColor Yellow
Write-Host "  uv run pyinstaller CubicAIO_Tool.spec" -ForegroundColor White
Write-Host ""

