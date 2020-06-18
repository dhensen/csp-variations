# Content-security-policy variations tested

Using django-csp to test some policies by using https://securityheaders.com/ to see which one gets a green/red badge.

## Variations tests

- Basic: `default-src 'self'`
  - green badge (see results/1...pdf)
- Report only: `default-src 'self'`
  - red badge (see results/2...pdf)
- Basic + unsafe inline: `default-src 'self' 'unsafe-inline'`
  - green badge (see results/3...pdf)

## Conclusion

It seems that you just need to have any kind of enforcing policy. So basicallt just have a Content-Security-Policy header, and the badge will be green F.W.I.W.
It does not say anything about the quality of the policy.
