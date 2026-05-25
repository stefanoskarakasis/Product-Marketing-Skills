# GitHub Upload Guide (Desktop App)

Step-by-step guide to upload the `go-to-market-strategy` plugin to GitHub using GitHub Desktop.

---

## Before You Start

**What you need:**
- GitHub Desktop installed ([download here](https://desktop.github.com))
- GitHub account
- The `go-to-market-strategy` folder on your computer

---

## Step 1: Download the Plugin Files

1. Download the entire `go-to-market-strategy` folder to your computer
2. Place it somewhere you can easily find (e.g., Desktop or Documents)

**Your folder should contain:**
```
go-to-market-strategy/
├── README.md
├── SKILL.md
├── INTEGRATION.md
├── config/ (4 files inside)
├── templates/ (3 files inside)
└── evals/ (1 file inside)
```

---

## Step 2: Open GitHub Desktop

1. Launch **GitHub Desktop**
2. Sign in to your GitHub account (if not already signed in)

---

## Step 3: Create a New Repository

### Option A: If you already have a PMM Skills repo

1. Click **File** → **Add Local Repository**
2. Navigate to your existing PMM skills folder
3. Click **Add Repository**
4. Skip to **Step 4**

### Option B: Create a new repository

1. Click **File** → **New Repository**
2. Fill in:
   - **Name:** `pmm-skills` (or whatever you want to call it)
   - **Description:** "Product Marketing plugins and tools"
   - **Local Path:** Choose where you want this on your computer
   - **Initialize with README:** ✓ Check this
3. Click **Create Repository**

---

## Step 4: Add the Plugin to Your Repository

1. **Open your repository folder in Finder (Mac) or File Explorer (Windows)**
   - In GitHub Desktop, click **Repository** → **Show in Finder/Explorer**

2. **Copy the `go-to-market-strategy` folder into your repository**
   - Drag the entire `go-to-market-strategy` folder into the repository folder

Your repository should now look like:
```
pmm-skills/
├── go-to-market-strategy/
│   ├── README.md
│   ├── SKILL.md
│   ├── INTEGRATION.md
│   ├── config/
│   ├── templates/
│   └── evals/
└── (other files/folders if you have them)
```

---

## Step 5: Commit the Changes

1. Go back to **GitHub Desktop**
2. You'll see all the new files listed on the left side
3. At the bottom left:
   - **Summary:** Type "Add go-to-market-strategy plugin"
   - **Description (optional):** "Brain-powered GTM strategy generator with tier assignment, self-learning, and skill routing"
4. Click **Commit to main**

---

## Step 6: Publish to GitHub

### If this is your first push:

1. Click **Publish repository** (top right)
2. Choose:
   - **Name:** (leave as is)
   - **Description:** (optional)
   - **Keep this code private:** ✓ Check if you want it private, uncheck for public
3. Click **Publish Repository**

### If you've already published this repo:

1. Click **Push origin** (top right)

---

## Step 7: Verify on GitHub.com

1. Click **Repository** → **View on GitHub**
2. You should see your `go-to-market-strategy` folder in the repository
3. Click into it to verify all files are there

---

## Done! 

Your plugin is now on GitHub.

**Repository URL will be:**
```
https://github.com/YOUR-USERNAME/pmm-skills
```

**Plugin folder will be at:**
```
https://github.com/YOUR-USERNAME/pmm-skills/tree/main/go-to-market-strategy
```

---

## Future Updates

When you make changes to the plugin:

1. Edit files on your computer (in the repository folder)
2. Open **GitHub Desktop**
3. Write a commit message describing what you changed
4. Click **Commit to main**
5. Click **Push origin**

Changes are now on GitHub.

---

## Troubleshooting

**"Repository not found" in GitHub Desktop**
→ Use **File** → **Add Local Repository** and select the folder

**Files not showing up in GitHub Desktop**
→ Make sure you copied files into the repository folder (use "Show in Finder/Explorer" to verify)

**Changes not appearing on GitHub.com**
→ Check that you clicked "Push origin" after committing

---

That's it. No terminal needed.
