# Student Command Complexity Evolution Report

## Executive Summary
An analysis of the shell histories from January 8 to February 10 reveals a stark learning curve among the participating teams. At the commencement of the competition, teams possessed minimal technical capability, exclusively relying on basic navigation and file-reading commands. Through a process of self-directed research (evidenced by heavy `tldr` tool usage), teams underwent a rapid skills progression, culminating in the execution of highly complex, multi-flag automated exploitation tools by early February.

## Data Analysis: The Complexity Timeline

The timeline of activities can be distinctly categorized into three phases of learning:

### Phase 1: Discovery & Basics (Early January)
At the start of the logs, participants demonstrated a near total inability to construct complex commands. During this period, the average complexity score hovered near zero.

*   **Jan 8-12 Metrics:** 43 commands on Day 1, ramping up as they began mapping the network. The average score remains extremely low, as they struggle with basic syntax. 
*   **Behavioral Note:** Participants were figuring out target boundaries, checking their own IP addresses, and heavily relying on built-in tool help menus because they did not yet know how to construct exploits.
*   **Utility Usage Examples:**
    *   **Network Mapping (`nmap`):** Struggling with flags or executing simple blanket sweeps (`nmap -sV -p 1-65535 -T 10.0.1.159`)
    *   **Enumeration (`enum4linux`):** Entirely limited to reading documentation (`enum4linux --help`, `enum4linux --help | less`)
    *   **Exploitation (`hydra`):** Malformed syntax or incomplete commands (`hydra -l root -P usr/share/wordlists/rockyou.txt`)

### Phase 2: The Learning Phase (Mid-to-Late January)
By mid-to-late January, teams began encountering roadblocks that forced them to adapt. During this period, we observe a steady volume of `tldr` queries, corresponding with the initial drops of more sophisticated commands. Teams began stringing commands together using paths, redirects, and basic tool invocations.

*   **Jan 20-27 Metrics:** Command complexity averages increased to `0.35`, with approximately **20-24%** of commands triggering the complexity threshold. 
*   **Behavioral Note:** Students transitioned from passive reading to active system enumeration and early exploitation attempts, correctly applying basic flags to tools.
*   **Utility Usage Examples:** 
    *   **Enumeration (`enum4linux`):** Correctly targeting users and hosts (`enum4linux -a -u ember -p password 10.100.7.46`)
    *   **Database Attacks (`sqlmap`):** Basic table enumeration (`sqlmap -u 10.100.7.45/panels.php?id=1" -D information_schema --tables"`)
    *   **Fuzzing (`ffuf`):** Applying wordlists (`ffuf -c -w /usr/share/wfuzz/wordlist/Injections/All_attack.txt -u http://10.100.7.45/FUZZ -fc 200`)

### Phase 3: Advanced Exploitation (Early February)
By week four, teams had effectively shed their novice behaviors. They successfully integrated their research into heavily nested, complex structural syntax required by penetration testing tools. 

*   **Feb 2-3 Metrics:** This phase represents the peak of sustained technical complexity. The average complexity score skyrocketed to `0.630`, with nearly **50% (48.2%)** of all executed commands classified as highly complex.
*   **Behavioral Note:** Teams are confidently wielding automated attack frameworks requiring extensive familiarity with specific target applications.
*   **Utility Usage Examples:**
    *   **Database Extraction (`sqlmap`):** Extracting specific columns from deeply nested schemas (`sqlmap -u 10.100.7.45/panels.php?id=1" -D pyrewatch -T thermal_readings --columns"`)
    *   **Active Directory Enumeration (`nxc`):** Executing credentialed network sweeps (`nxc smb 10.100.7.46 -u krbtgt -p PNqRrcXU4W0eWaE1MGvy`)
    *   **File Share Traversing (`smbclient`):** Authenticated script browsing (`smbclient //10.100.7.46/Scripts --user Ember`)

## Conclusion
The data unequivocally confirms that teams entered the competition without the underlying knowledge required to execute complex attacks. Over a 5-week timespan, they successfully bootstrapped their capabilities from `ls` and `cat` to utilizing parameterized web application fuzzing and database extraction tools.