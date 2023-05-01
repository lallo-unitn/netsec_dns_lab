$TTL   60000
@               IN      SOA     dnswebsite.website.com.   root.dnswebsite.website.com.  (
                        2006031201 ; serial
                        28800 ; refresh
                        14400 ; retry
                        3600000 ; expire
                        0 ; negative cache ttl
                        )

@        			IN      NS      dnswebsite.website.com.
dnswebsite.website.com. 	IN	A 	192.168.1.6

trusted 	IN      A       192.168.1.4
