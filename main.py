from pyscript import display, document

def generate_profile(event):
	name = document.getElementById("name").value
	age = document.getElementById("age").value
	school = document.getElementById("school").value

	if not name or not age or not school:
			return
	
	document.getElementById("output").innerText = ""
	
	message = f"""👤 <span style="font-weight: bold;">Student Profile</span>
	<br> Name: {name}
	<br> Age: {age}
	<br> School: {school}

	<br> <br> 📋 <b>Notes:</b>
	<br> {name} is {age}, and they study <br> at {school}! 🔥
	"""

	document.getElementById("output").innerHTML = message

document.getElementById("generate-btn").addEventListener("click", generate_profile)
