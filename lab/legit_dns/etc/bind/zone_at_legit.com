$TTL   60000
@               IN      SOA     legit.com.    ns.legit.com. (
                        2006031201 ; serial
                        28800 ; refresh
                        14400 ; retry
                        1 ; expire
                        0 ; negative cache ttl
                        )

@   1       IN      NS    ns.legit.com.

@   	1       IN      A     3.3.3.3
www 	1       IN      A     3.3.3.3
ns  	1       IN      A     3.3.3.2
web1 	1       IN      A     3.3.3.3
web2 	1       IN      A     3.3.3.4
*   	1       IN      A     3.3.3.3
