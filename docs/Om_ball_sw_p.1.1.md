## [Om Ball](https://github.com/jpiersongd/soundmotion/blob/main/docs/Om_ball.md) p1.1 - Given a single volume input value, make an Om sound correlating in volume.

### Background  - user scenarios:
- Based on Acceleration measurements only
- Ball is sitting, not moving, no sound
- Ball is nudged, an Om sound emits as long as it continues moving, then stops
- Ball is picked up, Om sound builds up power as ball is moved. More vigorous movement cause more volume in Om sound
- All metrics will be mapped to a 0 to 100 range
	
### Acceptance Criteria:
- Be called from Python on a Raspberry Pi 3 or 4
- Om sound is reasonably pleasant, though monotone
- Volume output directly corresponds to input value
- Update sound volume a minimum of 10 times a second
- Output to Bluetooth speakers
