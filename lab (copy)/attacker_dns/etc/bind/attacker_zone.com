$TTL   60000
@               IN      SOA     attacker.com.    ns.attacker.com. (
                        2006031201 ; serial
                        28800 ; refresh
                        14400 ; retry
                        3600000 ; expire
                        0 ; negative cache ttl
                        )

@       IN      NS    ns.attacker.com.

@       IN      A     1.1.1.4
www     IN      A     1.1.1.4
ns      IN      A     1.1.1.3
*       IN      A     1.1.1.4
