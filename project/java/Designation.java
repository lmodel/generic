package None;

import java.util.List;
import lombok.*;






/**
  representation for someone or something by a sign that denotes it
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Designation extends NamedThing {

  private String hasTextValue;
  private List<InformationContentEntity> identifies;

}