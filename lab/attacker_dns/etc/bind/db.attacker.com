$TTL   60000
@               IN      SOA     ns1.legit.com.    root.ns1.legit.com. (
                        2006031201 ; serial
                        28800 ; refresh
                        14400 ; retry
                        3600000 ; expire
                        0 ; negative cache ttl
                        )

@        	IN      NS      ns1.legit.com.
ns1.legit.com.	IN	A 	192.168.1.6

web1 	IN 	A	192.168.1.7
