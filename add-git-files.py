import subprocess
import os

def run_git_commands():
    # Run 'git add .' to stage all changes
    subprocess.run(['git', 'add', '.'])

    # Get the list of added files
    added_files = subprocess.check_output(['git', 'diff', '--cached', '--name-only']).decode('utf-8').splitlines()

    if not added_files:
        print("No changes to commit.")
        return

    # Create commit message
    commit_message = "feat: " + " and ".join([f'{i + 1:02d}-{os.path.basename(file)}' for i, file in enumerate(added_files)])

    # Commit changes
    subprocess.run(['git', 'commit', '-m', commit_message])

    # Push changes
    subprocess.run(['git', 'push'])

    print("Git commands executed successfully.")

# Run the script
run_git_commands()
