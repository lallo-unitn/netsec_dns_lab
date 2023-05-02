$TTL   60000
@               IN      SOA     dnscom.com.    ns1.dnscom.com. (
                        2006031201 ; serial
                        28800 ; refresh
                        14400 ; retry
                        3600000 ; expire
                        0 ; negative cache ttl
                        )
@                   	IN      NS      dnscom.com.
dnscom.com.        	IN      A       192.168.1.15

legit.com.           	IN      NS      ns1.legit.com.
ns1.legit.com.		IN      A       192.168.1.11
