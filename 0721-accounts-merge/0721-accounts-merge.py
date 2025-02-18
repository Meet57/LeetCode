class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def find(x): # finding the parent node
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y): #making the 2 parent node same 
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        # Initialize Data Structures

        # parent: Maps each email to its own parent (initially itself).
        # email_to_name: Maps each email to the corresponding user name.

        parent = {}
        email_to_name = {}

        # Step 1: Initialize the parent for each email and store the name for each email
        # Union-Find Operations

        # Iterate through each account, assigning the first email as the parent.
        # Use union() to connect all emails within the same account under a common parent.
        for account in accounts:
            name = account[0]
            first_email = account[1]

            if first_email not in parent:
                parent[first_email] = first_email
            email_to_name[first_email] = name

            for email in account[2:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)

        # parent: email -> email and merged nodes with comman parent
        # email_to_name : email -> name

        # Step 2: Group emails by their root email
        # Find the root parent for each email and group them accordingly. 
        root_to_emails = {}
        for email in parent:
            root = find(email)
            if root not in root_to_emails:
                root_to_emails[root] = []
            root_to_emails[root].append(email)
        
        # Step 3: Format the result
        # Retrieve the name from email_to_name.
        # Sort emails and return the merged accounts.
        result = []
        for emails in root_to_emails.values():
            name = email_to_name[emails[0]]
            result.append([name] + sorted(emails))
        
        return result