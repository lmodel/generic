package None;

import java.util.List;
import lombok.*;






/**
  an item that holds summary level information about a dataset.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DatasetSummary extends InformationContentEntity {

  private String sourceWebPage;
  private String sourceLogo;

}