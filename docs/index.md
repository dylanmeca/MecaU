# ☣ MecaU 🦠
[![Build Status](https://img.shields.io/github/stars/dylanmeca/MecaU.svg)](https://github.com/dylanmeca/MecaU)
[![License](https://img.shields.io/github/license/dylanmeca/MecaU.svg)](https://github.com/dylanmeca/MecaU/blob/main/LICENSE)
[![dylanmeca](https://img.shields.io/badge/author-dylanmeca-green.svg)](https://github.com/dylanmeca)
[![Python](https://img.shields.io/badge/language-Python%20-yellow.svg)](https://www.python.org)
![mecau](https://github.com/dylanmeca/MecaU/raw/main/logo.png)

MecaU is a security program designed to scan files for malware. It uses a database of known virus hashes and will compare the hash of each file 
on the system against the database to determine if it is infected. If an infected file is detected, the user has the choice to remove the malware or not. 
The program uses the OS Python library to walk through the files on the system and the hashlib library to calculate the hash of each file. 
The requests library is used to download the hash database from a server. MecaU is an effective tool to keep the system safe and protected against malware.

More information in the [Mecau Repository](https://github.com/dylanmeca/MecaU).

<!-- LikeBtn.com BEGIN -->
<span class="likebtn-wrapper" data-theme="angular" data-ef_voting="buzz" data-white_label="true"></span>
<script>(function(d,e,s){if(d.getElementById("likebtn_wjs"))return;a=d.createElement(e);m=d.getElementsByTagName(e)[0];a.async=1;a.id="likebtn_wjs";a.src=s;m.parentNode.insertBefore(a, m)})(document,"script","//w.likebtn.com/js/w/widget.js");</script>
<!-- LikeBtn.com END -->

<div id="disqus_thread"></div>
<script>
    /**
    *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
    *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables    */
    /*
    var disqus_config = function () {
    this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    */
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://dylan14567.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
