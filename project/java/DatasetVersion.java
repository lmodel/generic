package None;

import java.util.List;
import lombok.*;






/**
  an item that holds version level information about a dataset.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DatasetVersion extends InformationContentEntity {

  private Dataset hasDataset;
  private String ingestDate;
  private DatasetDistribution hasDistribution;

}