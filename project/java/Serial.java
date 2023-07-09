package None;

import java.util.List;
import lombok.*;






/**
  This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Serial extends Publication {

  private String isoAbbreviation;
  private String volume;
  private String issue;

}