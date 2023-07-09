package None;

import java.util.List;
import lombok.*;






/**
  A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Attribute extends NamedThing {

  private OntologyClass hasAttributeType;
  private List<QuantityValue> hasQuantitativeValue;
  private NamedThing hasQualitativeValue;

}