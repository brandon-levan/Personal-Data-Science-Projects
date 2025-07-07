# Vercel Deployment Guide

## Prerequisites
- GitHub account
- Vercel account (free at vercel.com)

## Local Testing
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app locally:
   ```bash
   python app.py
   ```

3. Open http://localhost:5000 in your browser

## Deploy to Vercel

### Option 1: GitHub Integration (Recommended)
1. Push this folder to a GitHub repository
2. Go to [vercel.com](https://vercel.com) and sign in
3. Click "New Project"
4. Import your GitHub repository
5. Vercel will automatically detect it's a Python app
6. Click "Deploy"

### Option 2: Vercel CLI
1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy from the project directory:
   ```bash
   vercel
   ```

## Configuration
The `vercel.json` file is already configured for this Flask app:
- Routes all requests to `app.py`
- Uses Python runtime
- Automatically handles WSGI

## Environment Variables
If you need to add environment variables later:
1. Go to your Vercel project dashboard
2. Navigate to Settings → Environment Variables
3. Add any required variables

## Custom Domain
After deployment:
1. Go to your Vercel project dashboard
2. Navigate to Settings → Domains
3. Add your custom domain

## Troubleshooting
- If deployment fails, check the Vercel logs in your dashboard
- Ensure all dependencies are in `requirements.txt`
- The app must be accessible at the root route (`/`) 