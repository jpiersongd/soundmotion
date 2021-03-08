## [Om Ball](https://github.com/jpiersongd/soundmotion/blob/main/docs/Om_ball.md) p1.1- Emulate a single volume input value, call the Om soundware function with value correlating to volume.

### Background - user scenarios:
Based on Acceleration measurements only
- Ball is sitting, not moving, no sound
- Ball is nudged, an Om sound emits as long as it continues moving, then stops
- Ball is picked up, Om sound builds up power as ball is moved. More vigorous movement cause more volume in Om sound
- All metrics will be mapped to a 0 to 100 range
	
### Acceptance Criteria:
- In Python, emulate calling the 9-axis 10 times a second on a Raspberry Pi 3 or 4
- Call the soundware function with one metric value for acceleration
- Value is mapped to a range of 0 to 100
  
