import os
"""
How I am generating the man page text file to be used for context. 
"""
# Define the list of programs to search for and their descriptions
programs = {
    'nmap': 'A powerful network scanning tool used for network discovery, vulnerability scanning, and identifying open ports and services on target systems.',
    'metasploit': 'A widely-used penetration testing framework that automates the process of exploiting known vulnerabilities in target systems and networks.',
    'wireshark': 'A network protocol analyzer that allows you to capture and analyze network traffic in real-time, which is useful for troubleshooting, security analysis, and protocol development.',
    'aircrack-ng': 'A suite of tools for 802.11 wireless network auditing, including tools for cracking WEP and WPA/WPA2 encryption keys.',
    'burpsuite': 'A popular web application security testing tool that provides various features for intercepting and modifying HTTP/HTTPS traffic, scanning web applications for vulnerabilities, and brute-forcing login forms.',
    'hydra': 'A fast and flexible network login cracker that supports many protocols, including HTTP, FTP, SSH, Telnet, and more.',
    'john': 'A powerful password-cracking tool that supports a wide range of hashing algorithms, including DES, MD5, and SHA.',
    'sqlmap': 'An automated SQL injection tool that can detect and exploit SQL injection vulnerabilities in web applications.',
    'nikto': 'A web server scanner that checks for misconfigurations, outdated software, and known vulnerabilities in web servers.',
    'zap': 'An easy-to-use web application security scanner that helps identify vulnerabilities in web applications.',
    'armitage': 'A graphical user interface for Metasploit that simplifies the process of selecting and launching exploits against target systems.',
    'set': 'A collection of social engineering tools designed to test an organization\'s defenses against human-based attacks, such as phishing, spear phishing, and other targeted attacks.',
    'maltego': 'A data mining and visualization tool that helps gather information about individuals, organizations, and infrastructure.',
    'snort': 'A powerful intrusion detection system (IDS) and intrusion prevention system (IPS) that can monitor and analyze network traffic to detect and prevent security breaches.',
    'hashcat': 'A fast and versatile password recovery tool that supports various hashing algorithms and can utilize GPUs for faster cracking.'
}

# Create the output directory if it does not exist
output_directory = os.path.join(os.getcwd(), 'man_pages')
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through each program in the list and search for it in /usr/bin
for program in programs.keys():
    command = f'grep -l {program} /usr/bin/*'
    result = os.popen(command).read().strip()

    # If the program is found, create a text file with its man page in the output directory
    if result:
        man_command = f'man {program} > {os.path.join(output_directory, program)}.txt'
        os.system(man_command)
        print(f'Created file: {program}.txt')
