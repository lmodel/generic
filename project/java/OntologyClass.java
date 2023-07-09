package None;

import java.util.List;
import lombok.*;






/**
  a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a base compatible KG can be considered both instances of base classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate base class.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OntologyClass  {

  private String id;

}