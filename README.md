## Rare Pizzas - NFT Data Hosting

# This process can be automated via the Pinata API once large numbers of content images need to be uploaded and managed

- Registered account on Pinata using hello@rarepizzas.com
  - Snax and Don Luv currently have this account password

- Browse 'Pinata Upload' tab

- Select 'upload directory' for single bundled upload

- Browse 'Pin Explorer' to view the pinned directory and contained contentIDs

- Drill down to each content ID to grab URI. Ensure URI doesn't specify folder to maintain unkown and rumer aspects of alternative pizza box art. 

- Grab contentID out of URI and prepend with 'https://ipfs.io/ipfs/{contentID} for box image URI 

- Populate box image URI to pizza_box.json files, 1 for each of the 100 pizza box types

- Upload and pin those pizza_box.json files, following the same process as above and getting ipfs URIs for each  

- Provide pizza_box.json URIs to smart contract team for inclusion in the pizza_reservations contract



box 55 was removed from the data set.  it is excluded from the render even though it actaully gets generated