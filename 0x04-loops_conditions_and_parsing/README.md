# 0x04. Bucles, condiciones y análisis

## Resources

- Loops sample
- Variable assignment and arithmetic
- Comparison operators
- File test operators
- Make your scripts portable

**Man or help**

- `env`
- `cut`
- `for`
- `while`
- `until`
- `if`

## Requirements

- All your files should end with a new line
- All your Bash script files must be executable
- You are not allowed to use `awk`
- Your Bash script must pass `Shellcheck` (version `0.3.3-1~ubuntu14.04.1` via apt-get) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

### Shellcheck

[Shellcheck](https://github.com/koalaman/shellcheck) is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! **All your Bash scripts must pass** `Shellcheck` **without any error or you will not get any points on the task**.

Shellcheck is available on the school’s computers. If you want to use it on your own computer, here is how to [install it](https://github.com/koalaman/shellcheck#installing).

Examples:

**Not passing `Shellcheck`:**
![Not passing](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png)

**Passing `Shellcheck`:**
![Passing](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png)

For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code `SC2034`, you can browse 
https://github.com/koalaman/shellcheck/wiki/SC2034.

### Tasks

## 0. Create a SSH RSA key pair
Read for this task:

- [Linux and Mac OS users](https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys)
- [Windows users](https://docs.rackspace.com/support/how-to/generating-rsa-keys-with-ssh-puttygen/)

man: `ssh-keygen`

You will soon have to manage your own **servers** concept page hosted on remote [data centers](https://www.youtube.com/watch?v=iuqXFC_qIvA&feature=youtu.be&t=46). We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

Requirements:

- Share your **public key** in your answer file `0-RSA_public_key.pub`
- Fill the `SSH public key` field of your intranet profile with the public key you just generated
- **Keep the private key to yourself in a secure location**, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
- If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase
SSH and RSA keys will be covered in depth in a later project.
- File: **[0-RSA_public_key.pub]()**

---
### 
