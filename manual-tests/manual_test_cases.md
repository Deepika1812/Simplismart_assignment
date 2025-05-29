# Manual Test Cases for GitHub QA Assignment

## 1. Sign Up and Login Tests

### Test Case 1.1: Create a New Account (Sign Up)

Objective: Verify that a user can successfully create a new GitHub account using valid information.

Preconditions: User is on the GitHub homepage (https://github.com)

Test Steps:

1. Click on the Sign up button or link on the homepage.  
   Expected Result: Sign up page loads with the registration form.

2. Enter a valid and unused Username.  
   Expected Result: Field accepts input and shows no error.

3. Enter a valid Email address.  
   Expected Result: Field accepts input and shows no error.

4. Enter a strong Password.  
   Expected Result: Field accepts input and password strength indicator updates.

5. Click on the Create account button.  
   Expected Result: User proceeds to the next step (e.g., email verification or preferences setup).

6. Complete verification steps such as captcha if presented.  
   Expected Result: Verification completes successfully.

7. Confirm account creation message or redirection to the dashboard.  
   Expected Result: User is redirected or shown confirmation of account creation.

Notes: Test with different password strengths and invalid emails to validate form validations.

---

### Test Case 1.2: Login with Valid Credentials

Objective: Verify that a user can log in with valid username/email and password.

Preconditions: User already has a registered GitHub account.

Test Steps:

1. Navigate to the GitHub login page.  
   Expected Result: Login page loads correctly.

2. Enter a valid Username or Email.  
   Expected Result: Field accepts input.

3. Enter the correct Password.  
   Expected Result: Field accepts input.

4. Click on the Sign in button.  
   Expected Result: User is successfully logged in and redirected to the dashboard/homepage.

---

### Test Case 1.3: Login with Invalid Credentials

Objective: Verify that the system handles login attempts with invalid credentials properly.

Preconditions: User is on the login page.

Test Steps:

1. Enter invalid or unregistered username/email.  
   Expected Result: Input accepted but authentication will fail.

2. Enter incorrect password.  
   Expected Result: Input accepted but authentication will fail.

3. Click on Sign in button.  
   Expected Result: Appropriate error message shown (e.g., "Incorrect username or password").

4. Verify that the user remains on the login page.  
   Expected Result: User is not logged in.

---

### Test Case 1.4: Validate Required Fields on Login Form

Objective: Ensure form validations work properly when required fields are empty.

Preconditions: User is on the login page.

Test Steps:

1. Leave the username/email field empty.  
   Expected Result: Error message or validation prompt displayed.

2. Leave the password field empty.  
   Expected Result: Error message or validation prompt displayed.

3. Try clicking Sign in with empty fields.  
   Expected Result: Login prevented and appropriate messages shown.

---

### Test Case 1.5: Validate Email Format on Sign Up

Objective: Verify the email field validates the format on the sign-up page.

Preconditions: User is on the Sign Up page.

Test Steps:

1. Enter invalid email formats (e.g., "user@domain", "userdomain.com", "user@.com").  
   Expected Result: Form shows validation error message.

2. Enter valid email format (e.g., "user@example.com").  
   Expected Result: No validation errors, field accepted.


## 2. Create a New Repository Tests

### Test Case 2.1: Create a New Public Repository

Objective: Verify that a user can create a new public repository via the GitHub web UI.

Preconditions: User is logged in to GitHub.

Test Steps:

1. Navigate to the “New Repository” page (e.g., via the + icon > New repository).  
   Expected Result: The "Create a new repository" page loads successfully.

2. Enter a valid and unique repository name.  
   Expected Result: Field accepts input with no errors.

3. (Optional) Enter a repository description.  
   Expected Result: Field accepts input.

4. Select the “Public” visibility option.  
   Expected Result: Public option is selected.

5. (Optional) Initialize repository with a README file by checking the box.  
   Expected Result: Checkbox is selected.

6. Click on the “Create repository” button.  
   Expected Result: Repository is created and user is redirected to the new repository’s main page.

---

### Test Case 2.2: Create a New Private Repository

Objective: Verify that a user can create a new private repository.

Preconditions: User is logged in and has the necessary permissions (for private repos).

Test Steps:

1. Navigate to the “New Repository” page.  
   Expected Result: Page loads successfully.

2. Enter a valid and unique repository name.  
   Expected Result: Field accepts input with no errors.

3. Select the “Private” visibility option.  
   Expected Result: Private option is selected.

4. (Optional) Initialize repository with a README file.  
   Expected Result: Checkbox is selected.

5. Click on the “Create repository” button.  
   Expected Result: Private repository is created and user is redirected to its page.

---

### Test Case 2.3: Validate Repository Name Field

Objective: Verify repository name field validates input properly.

Preconditions: User is on the “New Repository” page.

Test Steps:

1. Leave the repository name empty and attempt to create a repository.  
   Expected Result: Validation error message is shown indicating that the repository name is required.

2. Enter repository name with invalid characters (e.g., spaces, special characters like !@#).  
   Expected Result: Validation error message shown indicating invalid characters.

3. Enter a repository name that already exists under the user’s account.  
   Expected Result: Error message indicating repository name already taken.

4. Enter a very long repository name exceeding allowed character limit.  
   Expected Result: Validation error message shown or input prevented.

---

### Test Case 2.4: Verify Repository Settings after Creation

Objective: Verify repository settings such as name, description, and visibility after repository creation.

Preconditions: Repository has been successfully created.

Test Steps:

1. Navigate to the repository’s settings tab.  
   Expected Result: Settings page loads without error.

2. Verify the repository name matches the input during creation.  
   Expected Result: Repository name is displayed correctly.

3. Verify the repository description (if provided) matches input.  
   Expected Result: Description is displayed correctly.

4. Verify the visibility (public/private) is correctly set.  
   Expected Result: Visibility status matches selected option during creation.

---

### Test Case 2.5: Check Repository Creation Error Handling

Objective: Verify proper error handling for failed repository creation attempts.

Preconditions: User is on the new repository creation page.

Test Steps:

1. Try creating a repository without filling required fields.  
   Expected Result: Validation errors displayed, creation blocked.

2. Try to create a repository with invalid repository name formats.  
   Expected Result: Appropriate error messages displayed.

3. Attempt to create a repository with the same name as an existing one.  
   Expected Result: Error message about duplicate repository name.


## 3. Issue Tracking Tests

### Test Case 3.1: Create a New Issue

Objective: Verify that a user can create a new issue in a repository via the GitHub web UI.

Preconditions:  
- User is logged in.  
- User has access to the repository.

Test Steps:

1. Navigate to the target repository.  
   Expected Result: Repository main page loads successfully.

2. Click on the "Issues" tab.  
   Expected Result: Issues page loads, showing existing issues or a message if none exist.

3. Click on the "New issue" button.  
   Expected Result: New issue creation form loads.

4. Enter a descriptive **Title** for the issue.  
   Expected Result: Title field accepts input without errors.

5. Enter a detailed **Description** of the issue (optional but recommended).  
   Expected Result: Description field accepts input.

6. (Optional) Assign labels by clicking on "Labels" and selecting relevant tags.  
   Expected Result: Selected labels appear on the issue.

7. (Optional) Assign the issue to a user by clicking on "Assignees" and selecting a user.  
   Expected Result: Selected assignee is added to the issue.

8. Click on "Submit new issue" button.  
   Expected Result: Issue is created, and the user is redirected to the newly created issue page.

---

### Test Case 3.2: Edit an Existing Issue

Objective: Verify that a user can edit the title, description, labels, and assignees of an existing issue.

Preconditions:  
- User is logged in.  
- User has access to the repository and the issue.

Test Steps:

1. Navigate to an existing issue page in the repository.  
   Expected Result: Issue details page loads.

2. Click the "Edit" button near the issue title or description.  
   Expected Result: Fields become editable.

3. Modify the issue **Title** or **Description**.  
   Expected Result: Fields accept input.

4. Add or remove **Labels**.  
   Expected Result: Labels update accordingly.

5. Add or remove **Assignees**.  
   Expected Result: Assignees update accordingly.

6. Save the changes by clicking the "Save" or "Update" button.  
   Expected Result: Changes are saved, and the issue page reflects the updates.

---

### Test Case 3.3: Close and Reopen an Issue

Objective: Verify that a user can close and reopen issues.

Preconditions:  
- User is logged in.  
- User has access to the repository and issue.

Test Steps:

1. Navigate to an open issue.  
   Expected Result: Issue page shows the issue as open.

2. Click on the "Close issue" button.  
   Expected Result: Issue status changes to closed, visible on the page.

3. Click on the "Reopen issue" button.  
   Expected Result: Issue status changes back to open.

---

### Test Case 3.4: Verify Issue Listing and Filtering

Objective: Verify that issues are listed properly and filters (such as open/closed, labels, assignees) work as expected.

Preconditions:  
- User is logged in.  
- The repository has multiple issues with various states and labels.

Test Steps:

1. Navigate to the repository's "Issues" tab.  
   Expected Result: List of issues is displayed.

2. Use filters to view only "Open" issues.  
   Expected Result: Only open issues are displayed.

3. Use filters to view only "Closed" issues.  
   Expected Result: Only closed issues are displayed.

4. Filter issues by specific labels.  
   Expected Result: Only issues with selected labels are shown.

5. Filter issues by assignees.  
   Expected Result: Only issues assigned to selected users are shown.

6. Verify pagination if the number of issues exceeds one page.  
   Expected Result: Pagination controls appear and function correctly.

---

### Test Case 3.5: Verify Issue Notifications

Objective: Verify that users receive notifications on issue creation, updates, and comments.

Preconditions:  
- User is logged in and watching the repository or subscribed to notifications.

Test Steps:

1. Create a new issue in the repository.  
   Expected Result: Subscribed users receive notifications for the new issue.

2. Update an existing issue (edit title, description, labels).  
   Expected Result: Subscribed users receive update notifications.

3. Add a comment to an issue.  
   Expected Result: Subscribed users receive comment notifications.

---
## 4. Pull Request Workflow Tests

### Test Case 4.1: Create a New Pull Request

Objective: Verify that a user can create a pull request (PR) from a feature branch to the base branch.

Preconditions:  
- User is logged in.  
- User has a repository with at least two branches (e.g., main and feature branch).

Test Steps:

1. Navigate to the repository’s main page.  
   Expected Result: Repository page loads.

2. Click on the "Pull Requests" tab.  
   Expected Result: Pull Requests page loads showing existing PRs or empty state.

3. Click the "New pull request" button.  
   Expected Result: Branch comparison page loads.

4. Select the base branch (usually `main` or `master`).  
   Expected Result: Base branch is selected.

5. Select the compare branch (the feature branch you want to merge).  
   Expected Result: Compare branch is selected.

6. Review the changes and conflict status.  
   Expected Result: Diff is displayed; no conflicts if the branches can be merged cleanly.

7. Click "Create pull request".  
   Expected Result: PR creation form loads.

8. Enter a descriptive title and detailed description for the PR.  
   Expected Result: Fields accept input.

9. (Optional) Add reviewers, assignees, labels, or projects.  
   Expected Result: Selections saved.

10. Click "Create pull request" button.  
    Expected Result: PR is created and visible in the Pull Requests list.

---

### Test Case 4.2: Review a Pull Request

Objective: Verify that a user can review a pull request by viewing changes and adding comments or approval.

Preconditions:  
- PR exists and user has access to repository.

Test Steps:

1. Navigate to the "Pull Requests" tab.  
   Expected Result: List of PRs is visible.

2. Click on an open pull request to view details.  
   Expected Result: PR details page loads, showing changes and discussions.

3. Review the changed files using the diff view.  
   Expected Result: Code changes are displayed clearly.

4. Add inline comments on specific lines (optional).  
   Expected Result: Comments are added and displayed.

5. Leave an overall review comment.  
   Expected Result: Comment field accepts input.

6. Submit the review with options: Approve, Request changes, or Comment only.  
   Expected Result: Review status updates accordingly.

---

### Test Case 4.3: Handle Merge Conflicts in Pull Request

Objective: Verify that the system properly notifies users of merge conflicts and prevents merging until conflicts are resolved.

Preconditions:  
- PR exists with conflicting changes.

Test Steps:

1. Open a pull request with merge conflicts.  
   Expected Result: UI indicates merge conflicts clearly.

2. Attempt to merge the PR using the "Merge pull request" button.  
   Expected Result: Button is disabled or an error message is shown indicating conflicts must be resolved.

3. User should resolve conflicts locally or via GitHub UI if suppo

## 5. Navigation Between Repository Features Tests

### Test Case 5.1: Navigate Between "Code", "Issues", "Pull Requests", and "Actions" Tabs

Objective: Verify seamless navigation across main repository tabs.

Preconditions:  
- User is logged in.  
- User has access to the repository.

Test Steps:

1. Open the repository main page.  
   Expected Result: Repository’s "Code" tab loads by default.

2. Click on the "Issues" tab.  
   Expected Result: Issues page loads quickly and displays issue list or empty state.

3. Click on the "Pull Requests" tab.  
   Expected Result: Pull Requests page loads showing open PRs or message if none exist.

4. Click on the "Actions" tab.  
   Expected Result: Actions page loads showing workflow runs or empty state.

5. Switch back to the "Code" tab.  
   Expected Result: Code tab loads with repository files displayed.

---

### Test Case 5.2: Verify Page Loading Times

Objective: Ensure pages load within an acceptable time frame (e.g., under 3 seconds).

Preconditions: User is logged in with stable internet.

Test Steps:

1. Navigate to each tab ("Code", "Issues", "Pull Requests", "Actions") as in Test Case 5.1.  
   Expected Result: Each page loads within acceptable performance limits.

---

### Test Case 5.3: Pagination Verification in Issues and Pull Requests

Objective: Verify pagination works correctly when issues or pull requests exceed one page.

Preconditions:  
- Repository has more issues or PRs than fit on one page.

Test Steps:

1. Navigate to the "Issues" tab.  
   Expected Result: Pagination controls (Next, Previous, page numbers) appear.

2. Click on the pagination controls to navigate between pages.  
   Expected Result: Correct list of issues loads for each page.

3. Repeat steps 1 and 2 for the "Pull Requests" tab.  
   Expected Result: Pagination works correctly.

---

### Test Case 5.4: UI Consistency Across Repository Features

Objective: Verify consistent layout, branding, and UI elements across different tabs.

Preconditions: User is logged in.

Test Steps:

1. Navigate through "Code", "Issues", "Pull Requests", and "Actions" tabs.  
   Expected Result: Header, navigation menu, fonts, colors, and branding are consistent.

2. Verify that common buttons (e.g., "New Issue", "New Pull Request") are placed logically and styled uniformly.  
   Expected Result: Buttons have consistent style and positioning.

---

### Test Case 5.5: Responsive Design Check

Objective: Verify repository features render correctly on different screen sizes.

Preconditions: User is logged in.

Test Steps:

1. Open repository pages on desktop screen size.  
   Expected Result: UI elements display correctly.

2. Resize browser window or use device emulation to test on tablet and mobile screen sizes.  
   Expected Result: UI adjusts correctly with no broken layouts or overlapping elements.

---

