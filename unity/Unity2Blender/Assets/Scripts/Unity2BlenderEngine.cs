using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Unity2BlenderEngine : MonoBehaviour {

	public string host 	= "localhost";
	public int port 	= 3000;

	void Start () {
		
	}
	
	void Update () {
	
	}

	void OnGUI() {
		if(GUI.Button(new Rect(10, 10, 100, 30), "Call") ){
			StartCoroutine(RenderUsingCycles());
		}
	}

	void OnPreCommand(){

	}

	void OnPostCommand(){

	}
	
	public IEnumerator RenderUsingCycles(){
		Debug.Log("RenderUsingCycles");
		RenderCommand req  	= new RenderCommand(10);
		Camera cam = Camera.main;
		Transform t = GameObject.Find("watch").transform;

		//req.cam = new CameraProperties(cam.transform.position.x, cam.transform.position.y, cam.transform.position.z, cam.transform.eulerAngles.x, cam.transform.eulerAngles.y , cam.transform.eulerAngles.z);
		req.cam = new CameraProperties(t.position.x, t.position.z, t.position.y, t.eulerAngles.x, t.eulerAngles.y , t.eulerAngles.z);
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
