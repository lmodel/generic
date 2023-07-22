package None;

import java.util.List;
import lombok.*;






/**
  A operational entity is a control entity
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OperationalEntity extends System {

  private boolean isController;

}