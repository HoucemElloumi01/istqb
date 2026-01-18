# ========================================
#  Golden Fork - Test Suite Setup (Windows)
# ========================================

Clear-Host

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Golden Fork - Test Suite Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ----------------------------------------
# Check Python installation
# ----------------------------------------
Write-Host "Checking Python installation..." -ForegroundColor Yellow

if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonVersion = python --version
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
}
else {
    Write-Host "✗ Python not found. Please install Python 3.8 or higher" -ForegroundColor Red
    exit 1
}

# ----------------------------------------
# Create virtual environment
# ----------------------------------------
Write-Host ""
Write-Host "Creating virtual environment..." -ForegroundColor Yellow

if (Test-Path "venv") {
    Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
}
else {
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

# ----------------------------------------
# Activate virtual environment
# ----------------------------------------
Write-Host ""
Write-Host "Activating virtual environment..." -ForegroundColor Yellow

$activateScript = ".\venv\Scripts\Activate.ps1"
if (Test-Path $activateScript) {
    & $activateScript
    Write-Host "✓ Virtual environment activated" -ForegroundColor Green
}
else {
    Write-Host "✗ Could not find venv activation script" -ForegroundColor Red
    exit 1
}

# ----------------------------------------
# Install dependencies
# ----------------------------------------
Write-Host ""
Write-Host "Installing test dependencies..." -ForegroundColor Yellow

pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Failed to install dependencies" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Dependencies installed" -ForegroundColor Green

# ----------------------------------------
# Create .env file if it doesn't exist
# ----------------------------------------
Write-Host ""
Write-Host "Checking environment configuration..." -ForegroundColor Yellow

if (Test-Path ".env") {
    Write-Host "✓ .env file already exists" -ForegroundColor Green
}
else {
    if (Test-Path ".env.example") {
        Copy-Item ".env.example" ".env"
        Write-Host "✓ Created .env file from template" -ForegroundColor Green
        Write-Host "⚠ Please edit .env file with your application URL and credentials" -ForegroundColor Yellow
    }
    else {
        Write-Host "✗ .env.example not found" -ForegroundColor Red
        exit 1
    }
}

# ----------------------------------------
# Create output directories
# ----------------------------------------
Write-Host ""
Write-Host "Creating output directories..." -ForegroundColor Yellow

New-Item -ItemType Directory -Force -Path "reports" | Out-Null
New-Item -ItemType Directory -Force -Path "screenshots" | Out-Null

Write-Host "✓ Output directories created" -ForegroundColor Green

# ----------------------------------------
# Final message
# ----------------------------------------
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Edit .env file with your application URL" -ForegroundColor White
Write-Host "   notepad .env" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Ensure your Golden Fork application is running" -ForegroundColor White
Write-Host ""
Write-Host "3. Run the tests:" -ForegroundColor White
Write-Host "   pytest                                    # Run all tests" -ForegroundColor Gray
Write-Host "   pytest -m smoke                           # Run smoke tests" -ForegroundColor Gray
Write-Host "   pytest --html=reports/report.html         # Generate HTML report" -ForegroundColor Gray
Write-Host ""
Write-Host "4. View the HTML report:" -ForegroundColor White
Write-Host "   reports/report.html" -ForegroundColor Gray
Write-Host ""
Write-Host "For more information, see README.md" -ForegroundColor Cyan
Write-Host ""