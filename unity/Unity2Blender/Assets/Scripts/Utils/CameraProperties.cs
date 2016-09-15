using UnityEngine;
using System.Collections;

[System.Serializable]
public class CameraProperties{
	public float x;
	public float y;
	public float z;
	public float eulerX;
	public float eulerY;
	public float eulerZ;

	public CameraProperties(float _x, float _y, float _z, float _eulerX, float _eulerY, float _eulerZ){
		x = _x;
		y = _z;
		z = _y;
		eulerX = _eulerX;
		eulerY = _eulerY;
		eulerZ = _eulerZ;
	}
}