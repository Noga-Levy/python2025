"""
Written in April 2025 by Noga Levy.

This program retrieves domain information from Whois and prints it in the terminal.
To do this, it first takes the inputted website and does a quick and simple check to see if it at least has a period.
Until it does, the user is prompted to re-input. After that, the program goes through its main test, which is seeing if
it causes a URLError, HTTPError, or InvalidURL error. If it does, the program ends with an error message. If not, it
continues.
The next section of the program sends a request to Whois to retrieve the HTML information for that site. From there,
depending on whether the website exists on the Whois database or not, the code will retrieve the HTML code containing
the information and print it out using an f-string and the replace method.
In the final chunk of the code, it offers to take the user to the site they inputted, to which they can respond Y for
yes or N for no.
"""
import http.client
import urllib.request
import urllib.error
import webbrowser

website = input("What website do you want info on? Enter the link below\n")

# We start by taking the inputted website and doing a preliminary check to see if the website has a period, eliminating
# a few common invalid URLs ("example,com," "hello," perhaps a plain old space in an effort to break the program)
while "." not in website:
    website = input("Error: The inputted website is not valid. Please try again:\n")

# Next, we retrieve the Whois HTML information for that website, while also doing the main check for invalid URLs.
try:
    response = urllib.request.urlopen("https://www.whois.com/whois/" + website)
    page_source = str(response.read())

except (urllib.error.URLError, urllib.error.HTTPError, http.client.InvalidURL) as e:
    print(f"Error: {e}")
    exit(1)

# Using the same terms used in the HTML, we make a list containing all the information we want to find (in a readable
# fashion) and use a for loop to find their indexes in page_source, the code-made-string.
info_needed = ["Domain", "Registered On", "Expires On", "Updated On", "Status", "Name Servers"]
index = []

for i in info_needed:
    HTMLCode = f'<div class="df-label">{i}:</div>'  # Single dash quotes because the HTML code itself contains
    # double-dashed quotation marks.
    HTMLCodePos = page_source.find(HTMLCode)  # The string is how it looks in the HTML
    if HTMLCodePos == -1:  # .find() returns -1 if it can't find where the code is
        print("Error: Website not found in database. Ending program.")
        exit(1)

    else:
        index.append(HTMLCodePos + len(HTMLCode))  # .find() retrieves the beginning of the string--to find the index of
        # the end, we add the length to the original index

# Now, we make a new list that we will fill with the information we want to send to the user.
infoSend = []

# And here's how we'll fill it:
for j in range(len(index)):
    i = index[j]

    originalStr = page_source[i:page_source.find("</div>", i)]
    originalStr = originalStr[22:]  # Remove the uninteresting code before and after
    infoSend.append(originalStr)  # Add the information that we need, and now have, to infoSend.

# We print it out with an f-string and the method replace.
print(f"Domain : {infoSend[0]}\nRegistered : {infoSend[1]}\nExpires : {infoSend[2]}\nUpdated : {infoSend[3]}"
      f"\nStatus : {infoSend[4]}\nServers : {infoSend[5]}".replace("<br>", ", "))

# And finally, we decide whether to take the user to the site or not.
seeSite = input("\n\nDo you wish to visit the site? Respond with either Y for yes or N for no.\n")

if seeSite.lower() == "y":
    webbrowser.open(website)

elif seeSite.lower() == "n":
    print(f"Understood. You will not be sent to {website}. Ending program now.")

else:
    print(f"Your response was unclear. As such, you will not be sent to {website}. Ending program now.")
