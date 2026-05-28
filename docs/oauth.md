# Google OAuth Local Setup Guide

This guide provides step-by-step instructions on how to set up Google OAuth for local development and troubleshoot common authentication errors (such as 401 errors).

---

## 🚀 Step-by-Step Setup

Follow these steps to generate a Google Client ID and configure your local workspace.

### Step 1: Create a Google Cloud Project
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Log in with your Google account.
3. In the top-left project dropdown, click **New Project**.
4. Enter a project name (e.g., `SSOC-Contribution-Atelier`) and click **Create**.

---

### Step 2: Configure the OAuth Consent Screen
1. Navigate to **APIs & Services** > **OAuth consent screen** from the left navigation menu.
2. Select **External** as the User Type and click **Create**.
3. Fill in the required fields under **App information**:
   - **App name**: `Open Source Contribution Atelier (Local)`
   - **User support email**: *Your Gmail address*
   - **Developer contact information**: *Your Gmail address*
4. Click **Save and Continue**.
5. Under **Scopes**, click **Add or Remove Scopes**. Select `/auth/userinfo.profile` and `/auth/userinfo.email`. Click **Update** and then **Save and Continue**.
6. **CRITICAL STEP (Test Users):** Under **Test users**, click **+ Add Users** and add your own Gmail address (and any other emails you plan to test with). Since the app is in "Testing" mode, *only* listed test users will be allowed to log in.
7. Click **Save and Continue** to finish.

---

### Step 3: Create OAuth Client ID Credentials
1. Go to **APIs & Services** > **Credentials**.
2. Click **+ Create Credentials** at the top and select **OAuth client ID**.
3. In the **Application type** dropdown, select **Web application**.
4. Set the **Name** to `Atelier Local Development`.
5. Under **Authorized JavaScript origins**, click **+ Add URI** and enter:
   ```text
   http://localhost:5173
   ```
   > [!IMPORTANT]
   > Do **NOT** add a trailing slash `/` at the end of the URL. Google requires exact origin matching.
6. Click **Create** at the bottom.
7. A popup will appear with your **Client ID** and **Client Secret**. Copy the **Client ID** (it ends with `.apps.googleusercontent.com`).

---

### Step 4: Configure the Local Environment
1. In your project workspace, open the `frontend/` directory.
2. Create/edit the `.env` file (you can copy it from `.env.example`).
3. Add your copied Client ID:
   ```env
   VITE_GOOGLE_CLIENT_ID=your-client-id-here.apps.googleusercontent.com
   ```
4. Restart your frontend server (`npm run dev`) to load the new environment variable.

---

## 🛠️ Troubleshooting 401 Errors & Common Issues

If you encounter authentication issues, check the console and refer to the solutions below.

### 1. `401: invalid_client`
* **Symptoms:** The Google login popup closes instantly or displays an "Error 400: invalid_client" page.
* **Reason:** The Client ID configured in your `frontend/.env` is incorrect, contains typos, extra spaces, or the credential was deleted in the Google Cloud Console.
* **Solution:** 
  - Double-check `frontend/.env`. Make sure the value matches your Google Credentials page exactly and has no trailing spaces.
  - Ensure the client ID ends with `.apps.googleusercontent.com`.

### 2. `401: origin_mismatch` (or `idpiframe_initialization_failed`)
* **Symptoms:** The console displays `Error: origin_mismatch` or the login button fails to initialize.
* **Reason:** The URL you are using to access the frontend does not match the URL registered under **Authorized JavaScript origins**.
* **Solution:**
  - Check your browser's address bar. If you are accessing the app using `http://127.0.0.1:5173/`, switch to `http://localhost:5173/` (Google treats these as completely different origins!).
  - Go back to the Google Cloud Console > Credentials and ensure `http://localhost:5173` is spelled exactly correctly with **no trailing slash** and **no path**.

### 3. `Error: Access Blocked: app has not completed Google verification`
* **Symptoms:** A screen saying "Access Blocked: Project has not been verified" is displayed.
* **Reason:** The Google consent screen is in "Testing" mode, and the email you are trying to log in with is not listed under **Test users**.
* **Solution:**
  - Go to Google Cloud Console > **OAuth consent screen**.
  - Scroll down to the **Test users** section.
  - Click **Add Users** and enter the exact Gmail address you are using to sign in.

### 4. Third-Party Cookie Blocking
* **Symptoms:** The Google sign-in iframe fails to initialize or immediately throws an error in modern browsers (Chrome Incognito, Brave, Safari).
* **Reason:** Modern privacy protections block the third-party cookies that Google's auth library requires when running on a different domain (`localhost` vs `google.com`).
* **Solution:**
  - Allow third-party cookies for `accounts.google.com` in your browser settings.
  - If using Brave, disable Brave Shields temporarily for `localhost:5173`.
