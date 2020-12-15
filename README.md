# ETL-Project
October 2020 (version 1.51)
Update 1.51.1: The update addresses these issues.

Welcome to the October 2020 release of Visual Studio Code. As announced in the October iteration plan, we focused on housekeeping GitHub issues and pull requests as documented in our issue grooming guide.

We also worked with our partners at GitHub on GitHub Codespaces, which ended up being more involved than originally anticipated. To that end, we'll continue working on housekeeping for part of the November iteration.

During this housekeeping milestone, we also addressed several feature requests and community pull requests. Read on to learn about new features and settings.

Workbench
More prominent pinned tabs
Pinned tabs will now always show their pin icon, even while inactive, to make them easier to identify. If an editor is both pinned and contains unsaved changes, the icon reflects both states.

Inactive pinned tabs showing pin icons

Extension trees use custom hover
Instead of using the native tooltip in extension tree views, we now use a custom hover that is consistent cross-platform and fits better with the overall UX.

Custom tree hover

Install an extension without synchronizing
You can now install an extension without synchronizing it while settings sync is enabled.

Install extension without syncing

Theme: GitHub Light

Install an extension from Explorer
VS Code now supports installing an extension VSIX file from the Explorer by right-clicking on a VSIX file and choosing the Install Extension VSIX context menu item.

Input blur command
A new internal workbench.action.blur command is now available, which removes focus from any focusable input. You can assign a keyboard shortcut for this command in the Keyboard Shortcuts Preferences.

Integrated Terminal
Local Echo
Making modifications in the terminal traditionally requires information to be sent to the terminal process, processed, and returned to VS Code in order to be affected. This can be slow when working on a poor or distant connection to an SSH server or Codespace.

This release adds a "local echo" mode to the terminal, which attempts to predict modifications and cursor movements made locally and show them in the UI without requiring a round trip to the server. By default, predicted characters show as "dimmed":

Gif showing typing with 250ms latency where characters entered immediately are dimmed

There are two settings you can use to configure this:

terminal.integrated.localEchoLatencyThreshold configures the detected delay threshold, in milliseconds, at which local echo will activate. This can be set to 0 to turn on the feature all the time, or -1 to disable it. Defaults to 30.
terminal.integrated.localEchoStyle configures the style or color of local character, defaults to dim.
IntelliSense
Resizable suggestions
This milestone, we've made several improvements to the suggestions UI. First and foremost, it can now be resized. Drag the sides or corners to resize the control.

Resizable Suggestions control

Theme: GitHub Light, Font: FiraCode

The size of the suggestions list will be saved and restored across sessions. The size of the details pane is only saved per session, since that size tends to be more variable. Also, the editor.suggest.maxVisibleSuggestions setting has become obsolete.

Status bar for suggestions
The suggestions control can now also show its own status bar at the bottom of the window. Enable it using the editor.suggest.showStatusBar setting. It makes toggling details simpler, and shows if a completion supports inserting, replacing, or both.

Suggestions Status Bar

Theme: GitHub Light, Font: FiraCode

In the sample above, selecting "Insert" results in Math.floorceil and selecting "Replace" results in Math.floor.

The new editor.suggest.insertMode setting allows you to configure whether you prefer insert or replace. When a suggestion supports both, your preference will be the default.

Move cursor to select suggestions
Last but not least, you can now move the cursor while suggestions are showing. For instance, you can trigger suggestions at the end of a word, move left to see more suggestions, and then use replace to overwrite the word.

Moving cursor while suggestions are showing

Theme: GitHub Light

Emmet
Custom snippets in Emmet are back. Additionally, snippets now automatically refresh upon saving the snippets file or updating the emmet.extensionsPath setting.

Emmet custom snippets working again

Source Control
Source Control input box saves commit message history
This addresses a feature request to navigate SCM commit history. Press ↑ and ↓ to display the prior and next commits, respectively. To move directly to the first and last position of the input box, press Alt in conjunction with the corresponding arrow key.

After typing a message in the SCM input box, then staging and committing changes, pressing the up arrow reveals the message that was just committed

Git: Tag commands in submenu
Tag related Git commands have been added to the ... Git menu.

Git tags submenu

Git: Rebase command
A new Git: Rebase branch... command has been added which lets you rebase a branch using the UI.

Git: Recursive clone command
With the Git: Clone (Recursive) command, you can now recursively clone Git repositories, including its nested Git submodules.

Timeline: Emoji shortcode rendering
We now render emoji shortcodes, such as :smile:, in the Timeline View.

Timeline view with emoji

Languages
Markdown smart select
Expand and shrink selection in Markdown documents using the following new commands:

Expand: ⌃⇧⌘→
Shrink: ⌃⇧⌘←
Selection applies to the following, and follows a traditional hierarchical pattern:

Headers
Lists
Block quotes
Fenced code blocks
Html code blocks
Paragraphs
Smart select within a Markdown document expands from a block element, to the block element containing it, to the rest of the content under a header, to the header itself

Empty brace formatting option for JavaScript and TypeScript
The new javascript.format.insertSpaceAfterOpeningAndBeforeClosingEmptyBraces and typescript.format.insertSpaceAfterOpeningAndBeforeClosingEmptyBraces formatting configuration option controls if spaces are inserted between empty braces. The default value for these settings is true. For example, for the JavaScript:

class Foo {
    doFoo() { }
}
Setting "javascript.format.insertSpaceAfterOpeningAndBeforeClosingEmptyBraces": false and formatting the code results in:

class Foo {
    doFoo() {} // Notice that the space has been removed
}
Browser support
Download folders (Edge, Chrome)
Leveraging the new File System Access API, VS Code running in a browser can now offer a download action for folders from the File Explorer to download all files and folders to disk.

Download folder

Note: This requires a recent version of Microsoft Edge or Google Chrome.

Open Workspace notification
If you open a folder that contains .code-workspace files at the top level, you'll now see a notification asking you to open it. This was always the case in VS Code for desktop, and will now work in the browser too.

Open workspace notification

Prevent accidental close
A new setting window.confirmBeforeClose was added to show a confirmation dialog before closing or leaving the workbench.

Possible values are:

keyboardOnly The confirmation will only be shown when you use a keybinding to close (for example, ⌘W). (default)
always: The confirmation dialog will always be shown, even if you close from a mouse gesture.
never: The confirmation will never be shown.
Close confirmation dialog

Note: This setting may not cover all cases. Browsers may still decide to close a tab or window without confirmation.

Contributions to extensions
GitHub Pull Requests and Issues
Work continues on the GitHub Pull Requests and Issues extension, which allows you to work on, create, and manage pull requests and issues.

To learn about all the new features and updates, you can see the full changelog for the 0.21.0 release of the extension.

Remote Development
Work continues on the Remote Development extensions, which allow you to use a container, remote machine, or the Windows Subsystem for Linux (WSL) as a full-featured development environment.

Feature highlights in 1.51 include:

Ability to persist/reconnect to terminal sessions.
Improved port forwarding experience.
You can learn about new extension features and bug fixes in the Remote Development release notes.

Preview features
Preview features are not ready for release but are functional enough to use. We welcome your early feedback while they are under development.

Settings sync
Settings sync now synchronizes extensions' global state. Extensions will have to provide the state to sync using the newly introduced setKeysForSync API.

Remember proxy credentials
We are overhauling the login dialog that shows when a network connection requires authentication with a proxy. A new setting, window.enableExperimentalProxyLoginDialog: true, will enable this new experience that we plan to make the default in a future release.

Proxy Login

Theme: GitHub Light

The dialog will appear inside the VS Code window and offer a way to remember the credentials so that you do not have to provide them each time you start VS Code. Credentials will be stored in the OS standard credential store (keychain on macOS, Windows Credential Manager on Windows, and gnome keyring on Linux).

We still only show this dialog once per session, but might revisit this decision in the future. You will see the dialog appear again in case the credentials you selected to be remembered are not valid. Providing them again allows you to change them.

Please enable this option and let us know if something does not work as expected through our issue tracker.

TypeScript 4.1 beta support
VS Code supports the TypeScript 4.1 beta and nightly builds. The 4.1 update brings some new TypeScript language features, such as support for recursive conditional types, as well as tooling improvements. One focus area has been adding initial support for @see tags in JSDoc comments.

To start using the TypeScript 4.1 nightly builds, just install the TypeScript Nightly extension. Please share feedback and let us know if you run into any bugs with TypeScript 4.1.

Extension authoring
Updated extension samples
We've updated some of our extension samples to include VS Code default styles that are hooked up to our color theme tokens. This means that common elements (text, buttons, inputs) will be themeable and match the default styles in the product. Below are the extensions that include this:

custom-editor-sample
webview-sample
webview-view-sample
Webview style samples

Codicon colors in trees
With the finalization of the ThemeIcon color API, extension authors can use theme colors on codicons in custom tree views.

Tree view with icon colors

Sync Global State
Extensions can now sync their global state by providing the keys, whose values should be synchronized when Settings Sync is enabled, using the newly introduced setKeysForSync API in globalState memento.

/**
 * Set the keys whose values should be synchronized across devices when synchronizing user-data
 * like configuration, extensions, and mementos.
 *
 * Note that this function defines the whole set of keys whose values are synchronized:
 *  - calling it with an empty array stops synchronization for this memento
 *  - calling it with a non-empty array replaces all keys whose values are synchronized
 *
 * For any given set of keys this function needs to be called only once but there is no harm in
 * repeatedly calling it.
 *
 * @param keys The set of keys whose values are synced.
 */
setKeysForSync(keys: string[]): void;
Comment thread reply button visibility
Comment extensions can now control the visibility of the reply button in a comment thread with a new property, CommentThread#canReply. When it's set to false, users will not see the reply button or comment box in the comment thread.

Proposed extension APIs
Every milestone comes with new proposed APIs and extension authors can try them out. As always, we want your feedback. This is what you have to do to try out a proposed API:

You must use Insiders because proposed APIs change frequently.
You must have this line in the package.json file of your extension: "enableProposedApi": true.
Copy the latest version of the vscode.proposed.d.ts file into your project's source location.
You cannot publish an extension that uses a proposed API. There may be breaking changes in the next release and we never want to break existing extensions.

Folding range providers change event
Folding range providers can signal to the editor that folding ranges need to be updated using the onDidChangeFoldingRanges event.

For more details and to provide feedback, please use issue #108929.

Password APIs
As part of continued work on Authentication Providers, we have introduced API for storing and retrieving sensitive information. Internally, this acts as a wrapper of the keytar library that VS Code uses for storing secrets.

    /**
     * Retrieve a password that was stored with key. Returns undefined if there
     * is no password matching that key.
     * @param key The key the password was stored under.
     */
    export function getPassword(key: string): Thenable<string | undefined>;

    /**
     * Store a password under a given key.
     * @param key The key to store the password under
     * @param value The password
     */
    export function setPassword(key: string, value: string): Thenable<void>;

    /**
     * Remove a password from storage.
     * @param key The key the password was stored under.
     */
    export function deletePassword(key: string): Thenable<void>;

    /**
     * Fires when a password is set or deleted.
     */
    export const onDidChangePassword: Event<void>
Engineering
Making VS Code Trusted Types compliant
We have continued the effort to make VS Code "Trusted Types" compliant. The goal is to prevent DOM-based cross site scripting vulnerabilities. You can learn more about trusted types at the web.dev Trusted Types site and follow our progress in issue #103699.

Documentation
Getting started
We are focusing on ways to make getting started with the editor easier. We've created a new "Learn to Code" landing page on our website with coding packs and new content geared towards folks who are new to coding. We've also created new student-friendly videos and resources on the site at code.visualstudio.com/learn.

Learn to code

Partner extensions
Coding Pack for Python (Windows)
The Coding Pack for Python installs Python 3.8, specific Python libraries, VS Code, and essential extensions like Python and LiveShare, making it easy for new coders to get started. It is currently available for Windows.

New commands
Key	Command	Command ID
unassigned	Focus Left Editor Group (do not wrap around)	workbench.action.focusLeftGroupWithoutWrap
unassigned	Focus Right Editor Group (do not wrap around)	workbench.action.focusRightGroupWithoutWrap
unassigned	Focus Above Editor Group (do not wrap around)	workbench.action.focusAboveGroupWithoutWrap
unassigned	Focus Below Editor Group (do not wrap around)	workbench.action.focusBelowGroupWithoutWrap
unassigned	Focus Activity Bar	workbench.action.focusActivityBar
Notable fixes
43819: Windows: when deleting a folder with files that are in use, then there is no error message shown
71315: Should maintain row focus after deleting a file
96522: User input variables not working for launch configuration in multi-root workspace
100255: Moving a file should load the model directly with the contents it had before
108578: Extensions with a onDebugDynamicConfigurations are eagerly activated at startup in v1.50
109088: Send vscode.workspace.onWillCreateFiles/onDidCreateFiles events for folders
109226: Debug hover moves while expanding/collapsing
Thank you
Last but certainly not least, a big Thank You to the following people who contributed this month to VS Code:

Contributions to our issue tracking:

John Murray (@gjsjohnmurray)
Alexander (@usernamehw)
Andrii Dieiev (@IllusionMH)
ArturoDent (@ArturoDent)
Contributions to vscode:

Justin Steven (@justinsteven): (Fixed in 1.49.3) Fix for CVE-2020-16881 can be bypassed PR #107952
Ashkan (@a5hk): closes #97890 PR #108779
Daniel Huth (@Agreon): Add Non-Wrapping EditorGroup-focus actions PR #108071
Andrey Sinitsyn (@asn007): fix(git): fatal when adding, reverting files or cleaning repo on win32 [#108690] PR #108691
Jordan Bayles (@baylesj): Add Git: Clone Recursively option PR #109133
Takanori Oishi (@bicstone)
UI items are incorrect order when applying the language pack PR #109433
Git: Add tags to '...' menu PR #109282
Borja Zarco (@bzarco): Fix launch configuration input variable resolution. PR #97440
Dhairya Nadapara (@dhairyanadapara): added preserve case and excluse setting in FindInFile interface PR #107910
Evan Krause (@evangrayk): Don't focus editor when un-expanded comment is hidden PR #97101
Fons van der Plas (@fonsp): message "Would you like to stage all chages?" PR #109272
John Murray (@gjsjohnmurray): fix #108673 Put FileSystemProvider error message into settings.json create-failure notification PR #108694
matvii (@hodovani): Replace map with forEach PR #109217
Jean Pierre (@jeanp413)
Fixes middle-clicking on a notification sometimes pastes the contents of the clipboard PR #109349
Fixes cannot disable file auto save when configuration target is other than user PR #109278
Read file contents as stream in ChangeEncodingAction PR #108052
Fixes outline view element overflow PR #108038
Kenny Smith (@kjs3): Trash/delete keybinding for forward delete on MacOS PR #108863
Li Xueli (@mixj93): fix: Remove extra whitespace in the untitled editor label PR #108039
@Nafana: Markdown reference links starting with ^ should not be clickable PR #108015
Pierre Papin (@pi-r-p): fix download issues in webviews PR #108603
Rakib Fiha (@RakibFiha): Changed shebang same as code.sh PR #109372
Ryan Clarke (@ryanclarke): Add new property to IConfigurationPropertySchema PR #108120
Sebastian Andil (@selrond): Fix No Nerify typo inside git package PR #108329
Simon Siefke (@SimonSiefke): fix typo: eventLister -> eventListener PR #108066
Tomer Stav (@tomerstav)
Rebase current branch onto another branch PR #108913
Add optional parameter to showOptions called newEditorGroup PR #107555
Note: This ended up not being merged, but we appreciate the work nonetheless.
Tony Xia (@tony-xia): Persisten -> Persistent PR #108389
@turara: Add keybinding shortcut for "Preserve case" replace option PR #107597
@vivekmthr: CodeLens activated on mouse up #107736 PR #108323
Contributions to vscode-json-languageservice:

Albert Nigmatzianov (@bogem): Improve README PR #78
Contributions to vscode-html-languageservice:

Jaime Oliveira (@IxquitilisSaid): Update beautify-html wrap_attributes documentation PR #92
Nicholas Steven Darmawan (@steve1998): Implement Hover for HTML Entities PR #89
Contributions to vscode-css-languageservice:

@ShPelles: [scss] correctly identify an element with id (div#id) PR #222
Contributions to vscode-eslint:

Brandon Mills (@btmills): Add markdown to eslint.probe default docs PR #925
Brad Zacher (@bradzacher): support remote development by indicating this is a workspace-only extension PR #1084
Clément Tessier (@ctessier): fix typos in README.md PR #1105
Contributions to language-server-protocol:

@KamasamaK
Add missing capabilities for callHierarchy PR #1105
Add some missing items to change log PR #1106
Remy Suen (@rcjsuen): Correct the slash to textDocument/semanticTokens PR #1111
Andreas Matthias (@AndreasMatthias): Escape dollar signs. PR #1124
Contributions to vscode-emmet-helper:

Yasar Siddiqui (@yasarsid): For Emmet expansion of d: should expand to "display: block" instead of "display: grid" PR #35
Contributions to lsif-node:

Noah Santschi-Cooney (@Strum355): lsif-util: Fix #70 by replacing \" with " in vertex extra info sections PR #112
Contributions to debug-adapter-protocol:

Jonah Graham (@jonahgraham): Bug #122: requestId for ProgressStartEvent is an integer PR #123
Mathias Fußenegger (@mfussenegger): Add nvim-dap to tools page PR #140
Suzy Mueller (@suzmue): Update Go debug extension info in adapters.md PR #142
Ethan Reesor (@firelizzard18): Add byebug-dap and ruby-dap PR #144
Contributions to vscode-vsce:

James George (@jamesgeorge007): fix: handle unknown args PR #503
Contributions to vscode-js-debug:

hp8wvvvgnj6asjm7: Debugger does not work when running Node.js on an unsupported operating system PR #791
