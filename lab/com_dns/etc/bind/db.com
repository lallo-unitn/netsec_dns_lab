$TTL   60000
@               IN      SOA     dnsauthcom.com.    root.dnsauthcom.com. (
                        2006031201 ; serial
                        28800 ; refresh
                        14400 ; retry
                        3600000 ; expire
                        0 ; negative cache ttl
                        )
@                   	IN      NS      dnsauthcom.com.
dnsauthcom.com.        	IN      A       192.168.1.15

website.com.           	IN      NS      dnswebsite.website.com.
dnswebsite.website.com.	IN      A       192.168.1.11
