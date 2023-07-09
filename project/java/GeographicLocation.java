package None;

import java.util.List;
import lombok.*;






/**
  a location that can be described in lat/long coordinates
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GeographicLocation extends PlanetaryEntity {

  private Float latitude;
  private Float longitude;

}