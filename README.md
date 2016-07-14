# pusheen-stickers
Scripts to pull Pusheen/FB stickers and animate them

![Pusheen Typing](https://raw.githubusercontent.com/lhl/pusheen-stickers/master/gif/pusheen/144884865685780.gif)

No copyright intended, yo!
j/k, this is for fair use purposes.

## Implementation Notes
* First we use Web Inspector to view network connections and pull the graphql query for the stickers - it's not worth reversing/automating everything. We can just copy the results into `graphql-pusheen.json` and `graphql-pusheen-eats.json`.
* Analysing the actual image queries, it looks like we can just access the sprite sheet and ignore the sizing URLs to get the full size image. Sweet.
* Save w/ GraphQL id (no labels) and FRAMESxFRAMERATE-COLUMNSxROW 


## See also
Here's another great nerdy Pusheen project: https://github.com/motemen/pusheen-explorer
