#Simple test to see how well the model summarizes a portion of the tos
from langchain_ollama import ChatOllama


llm = ChatOllama(model="deepseek-r1:1.5b", temperature = 0)
llm_json_mode = ChatOllama(model="deepseek-r1:1.5b", temperature = 0, format = "json")

tos = """
Using our Services
What you can do. Subject to your compliance with these Terms, you may access and use our Services. In using our Services, you must comply with all applicable laws as well as our Sharing & Publication Policy⁠, Usage Policies⁠, and any other documentation, guidelines, or policies we make available to you. 
What you cannot do. You may not use our Services for any illegal, harmful, or abusive activity. For example, you may not:
Use our Services in a way that infringes, misappropriates or violates anyone’s rights.
Modify, copy, lease, sell or distribute any of our Services.
Attempt to or assist anyone to reverse engineer, decompile or discover the source code or underlying components of our Services, including our models, algorithms, or systems (except to the extent this restriction is prohibited by applicable law).
Automatically or programmatically extract data or Output (defined below).
Represent that Output was human-generated when it was not.
Interfere with or disrupt our Services, including circumvent any rate limits or restrictions or bypass any protective measures or safety mitigations we put on our Services.
Use Output to develop models that compete with OpenAI.
Software. Our Services may allow you to download software, such as mobile applications, which may update automatically to ensure you’re using the latest version. Our software may include open source software that is governed by its own licenses that we’ve made available to you.
Corporate domains. If you create an account using an email address owned by an organization (for example, your employer), that account may be added to the organization's business account with us, in which case we will provide notice to you so that you can help facilitate the transfer of your account (unless your organization has already provided notice to you that it may monitor and control your account). Once your account is transferred, the organization’s administrator will be able to control your account, including being able to access Content (defined below) and restrict or remove your access to the account. 
Third party Services. Our services may include third party software, products, or services, (“Third Party Services”) and some parts of our Services, like our browse feature, may include output from those services (“Third Party Output”). Third Party Services and Third Party Output are subject to their own terms, and we are not responsible for them.
"""

msg = llm.invoke(tos)

print(msg.content)

#Output:
#<think>
#Okay, so I'm trying to understand the Terms of Service for this service. Let me read through it again carefully.

#First, what can I do? It says I can access and use the services as long as I comply with applicable laws and our Sharing & Publication Policy, Usage Policies, etc. So that's good; no restrictions on using the service unless there are specific laws or policies in place.

#What I cannot do? There are several points here. First, I can't use it for illegal activities like hacking or misusing someone else's data. That makes sense because we're probably not involved in those 
#kinds of things.

#Second, I can't modify, copy, lease, sell, or distribute the services. So if I want to change how the service works or take copies of it, that's off-limits. Also, I can't reverse engineer the source code or look into our models, algorithms, or systems unless it's prohibited by law.

#Third, I can't automatically or programmatically extract data or output. That means I can't generate 
#content on my own without some assistance from us. It also says I can't represent that Output was human-generated when it wasn't. So if someone else made the output, I can't claim credit for it.        

#Fourth, I can't use Output to develop models that compete with OpenAI. That's interesting because OpenAI is a big company, so maybe there are some restrictions on how we can use their AI models.        

#Then there's software section. We allow downloads of mobile apps that update automatically. Some of these might be open source, governed by their own licenses. So if I download something from us, it could be using those licenses, which might have terms I need to consider.

#Corporate domains: If someone owns an email address for a company, we can transfer the account to them and provide notice. But once transferred, they can access our content and control my account. That's a bit tricky because it means if I'm using their services, I might be limited in how I use theirs. 

#Third party services include third-party software or products that might have Output features. We're 
#not responsible for their terms, so I should check those separately.

#Wait, let me make sure I got all the points right. The first bullet is about access and usage, second to eighth are restrictions on what I can't do. So the user can use it as long as they comply with laws and our policies, but not certain actions that could be illegal or misuse someone else's work.    

#I'm a bit confused about how third-party services fit in. If there are third parties contributing Output, does that mean we're responsible for their terms? Or do I have to check those separately?       

#Also, the software section mentions open source software with specific licenses. How does that affect my usage? Do I need to comply with any licensing terms when using such software?

#Third party output is mentioned as part of our services, so if they provide Output through third parties, we're not responsible for their content. That means I can't claim credit or use it without checking the source.

#I think I should also consider how these policies apply in different regions or countries. Are there 
#any specific laws that might affect my usage? Maybe some jurisdictions have stricter regulations on AI services.

#Another thing is the corporate domain part. If someone owns an email for a company, can they access our services? It seems like it's conditional, so I need to be aware of that when using their accounts.
#Overall, the Terms seem pretty comprehensive, but there are specific areas where I might have to comply with additional regulations or terms beyond what's stated here. I should review each section carefully and make sure all my activities fall within the scope allowed by these policies.
#</think>

#The Terms of Service outline the guidelines for using a service, emphasizing compliance with applicable laws and specific policies. Here's a structured summary:

#1. **Access and Usage**: You can access and use the service as long as you comply with applicable laws and our Sharing & Publication Policy, Usage Policies, etc.

#2. **Notable Restrictions**:
#   - **Illegal or Misuse Activities**: Use the service for illegal, harmful, or abusive activities.  
#   - **Modification, Copying, Leasing, Selling Output**: Do not modify, copy, lease, sell, or distribute the services unless prohibited by law.
#   - **Reverse Engineering and Source Code**: Do not automatically or programmatically extract data or output, nor claim credit for Output without verification.
#   - **Model Competition**: Use Output to develop models that compete with OpenAI, though this may have specific terms from OpenAI.

#3. **Software Section**:
#   - **Mobile Apps**: You can download updates, but some might be open source governed by their own licenses.
#   - **Corporate Domains**: If an email is owned by a company, it may be transferred to them with notice unless the company has already provided monitoring.

#4. **Third Party Services**:
#   - Third-party software or products may include Output features; we are not responsible for their terms.

#5. **Conditional Access**:
#   - Use of accounts from owners of corporate emails is conditional and subject to notice if transferred.

#6. **Licensing Considerations**:
#   - Open source software with specific licenses may require compliance with those terms when using such software.

#7. **Regional Compliance**: Laws in different regions may vary, so check applicable laws for specific regulations affecting your usage.

#In summary, while the Terms are comprehensive, specific areas like third-party 
#services and corporate domains require careful consideration of applicable laws and policies. 
#Always verify compliance with local regulations and policy terms when using these services.

