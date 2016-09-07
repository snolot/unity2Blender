using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Unity2BlenderEngine : MonoBehaviour {

	public string host 	= "localhost";
	public int port 	= 3000;

	void Start () {
		StartCoroutine(RenderUsingCycles());
	}
	
	void Update () {
	
	}

	public IEnumerator RenderUsingCycles(){
		Debug.Log("RenderUsingCycles");
		RenderCommand req  	= new RenderCommand(10);
		string jsonString 	= req.ToJSON();

		Debug.Log(jsonString);

		var encoding 		= new System.Text.UTF8Encoding();
		var postHeader 		= new Dictionary<string, string>();
   
		postHeader.Add("Content-Type", "application/json");
		postHeader.Add("Content-Length", jsonString.Length.ToString());

 		WWW www = new WWW("http://"+host+":"+port+"/render", encoding.GetBytes(jsonString), postHeader);
        
 		yield return www;
 		Debug.Log(www.text);
	}

	public void SaveAsObj(string filename){

	}
}
