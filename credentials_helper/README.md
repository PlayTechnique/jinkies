# What is this script?

It's a quick tool I threw together to help generate credentials from templates. Jenkins has specific requirements 
for its credentials file format, and I thought it was better to provide a way to generate these credentials files 
than to force user to learn all of the file formats.

Right now, the supported file format is plain-text. This is suitable for logging in to github.
Write the file out to somewhere on the file system that you can mount it into jinkies from.