package None;

import java.util.List;
import lombok.*;






/**
  an item that holds distribution level information about a dataset
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DatasetDistribution extends InformationContentEntity {

  private String distributionDownloadUrl;

}