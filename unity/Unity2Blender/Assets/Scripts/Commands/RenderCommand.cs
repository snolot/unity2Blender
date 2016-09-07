using UnityEngine;
using System.Collections;

[System.Serializable]
public class RenderCommand : BasicCommand {
	public string output = "png";

	public int hours;
	public int minutes;

	public RenderCommand(int _priority){
		name 		= "RenderCommand";
		priority 	= _priority;

		var now = System.DateTime.Now;
		hours = now.Hour;
		minutes = now.Minute;
	}

	public string ToJSON(){
		return JsonUtility.ToJson(this);
	}
}
