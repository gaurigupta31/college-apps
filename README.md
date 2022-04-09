# cockroach-scripts + authentication process :cockroach: :key:

For the database, we're making use of CockroachDB - a cloud-based, distributed SQL database. To recreate the DB, follow these steps:

1. Sign up for a free account on [Cockroach Labs](https://cockroachlabs.cloud/signup)
2. Login and create a free cluster. Name it what you want and choose a cloud provider of your choice.
3. Follow the steps post creation of the cluster to access the database remotely - this will typically involve in installing the Cockroach DB driver locally, ensuring the certificates are installed in the correct place, and running the `cockroach` command to connect to the instance locally.
4. We are making use of only one table, find the insert statement [here](insert-query.sql)

---

## Understanding the authentication process

As privacy conscious individuals, we ourselves are always cautious before signing up on or providing our personal information to any unknown website. To ensure security, we make use of an implementation of Zero Proof Knowledge (ZPK) called Secure Remote Password (SRP). 
Here is a simple understanding of what we do and how we register and authenticate a user:

1. Once the client enters the username and password, we generate `salt` (a random string). Using the username, password, and salt, we generate `x` by passing these values in something called a Key Derivation Function (KDF) - this is a trapdoor function.
2. Further, we generate another random string called the `verifier` using `x` and `SRP groups` which are of different types - 1024 bit, 2048 bit, etc
3. At the server side, we store `salt` and `verifier`
4. For authentication, the client generates a (private key) and A (public key) using the SRP groups. Similar, the server generates b (private key) and B (public key) using the SRP groups. `(x, a, B)` from the client's side and `(verifier, b, A)` from the server's side present the same value using different calculations.

---

If you're interested in reading more about SRP, here are some links that we referred to:
1. [The Secure Remote Password Protocol](http://srp.stanford.edu/ndss.html)
2. [What Is Secure Remote Password (SRP) Protocol and How to Use It?](https://medium.com/swlh/what-is-secure-remote-password-srp-protocol-and-how-to-use-it-70e415b94a76)
3. [SRP Python Package Documentation](https://pythonhosted.org/srp/srp.html)
4. [pysrp provides a Python implementation of the Secure Remote Password protocol](https://github.com/cocagne/pysrp)