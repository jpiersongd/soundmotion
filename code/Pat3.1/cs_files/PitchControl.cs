using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Audio;

public class PitchControl : MonoBehaviour
{
    [SerializeField] string _pitchshifterParameter = "Master Pitch";
    public AudioMixer _mixer;
    public Slider _slider;




    private void Awake()
    {


        _slider.onValueChanged.AddListener(HandleSliderValueChanged);


    }

    private void HandleSliderValueChanged(float value)

    {
        _mixer.SetFloat(_pitchshifterParameter, value);
    }



}