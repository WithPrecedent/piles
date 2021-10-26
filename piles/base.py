"""
base: base classes for extensible, flexible, lightweight data structures
Corey Rayburn Yung <coreyrayburnyung@gmail.com>
Copyright 2021, Corey Rayburn Yung
License: Apache-2.0

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

Contents:
    Proxy (Container): basic wrapper for a stored python object. Dunder methods 
        attempt to intelligently apply access methods to either the wrapper or 
        the wrapped item.   
    Bunch
          
To Do:
    Integrate ashford Kinds system when it is finished.
    Add in 'beautify' str representations from amos once those are finished.
    
    
"""
from __future__ import annotations
import abc
import collections
from collections.abc import (
    Collection, Container, Hashable, Iterator, MutableMapping, MutableSequence, 
    Sequence, Set)
import dataclasses
from typing import (
    Any, Callable, ClassVar, Optional, Type, TYPE_CHECKING, TypeVar, Union)

from . import check
from . import tracking
from . import utilities

if TYPE_CHECKING:
    from . import bunch
    from . import graph
    from . import manifest
    from . import proxy
    from . import tree  

           
@dataclasses.dataclass
class Composite(tracking.RegistrarFactory, abc.ABC):
    """Base class for composite data structures.
    
    Args:
        contents (Collection[Any]): stored collection of nodes and/or edges.
        registry (ClassVar[MutableMapping[str, Type[Any]]]): key names are str
            names of a subclass (snake_case by default) and values are the 
            subclasses. Defaults to an empty dict.  
                                     
    """  
    contents: Collection[Any]
    registry: ClassVar[MutableMapping[str, Type[Any]]] = {}
    
    """ Required Subclass Properties """
        
    @abc.abstractproperty
    def endpoint(self) -> Optional[Union[proxy.Node, proxy.Nodes]]:
        """Returns the endpoint(s) of the stored composite object."""
        pass
 
    @abc.abstractproperty
    def root(self) -> Optional[Union[proxy.Node, proxy.Nodes]]:
        """Returns the root(s) of the stored composite object."""
        pass

    @abc.abstractproperty
    def adjacency(self) -> graph.Adjacency:
        """Returns the stored composite object as an graph.Adjacency."""
        pass

    @abc.abstractproperty
    def edges(self) -> graph.Edges:
        """Returns the stored composite object as an graph.Edges."""
        pass
       
    @abc.abstractproperty
    def matrix(self) -> graph.Matrix:
        """Returns the stored composite object as a graph.Matrix."""
        pass
       
    @abc.abstractproperty
    def nodes(self) -> proxy.Nodes:
        """Returns the stored composite object as a proxy.Nodes."""
        pass
        
    @abc.abstractproperty
    def pipeline(self) -> manifest.Pipeline:
        """Returns the stored composite object as a manifest.Pipeline."""
        pass
        
    @abc.abstractproperty
    def pipelines(self) -> manifest.Pipelines:
        """Returns the stored composite object as a manifest.Pipelines."""
        pass
            
    @abc.abstractproperty
    def tree(self) -> tree.Tree:
        """Returns the stored composite object as a tree.Tree."""
        pass
                 
    """ Required Subclass Class Methods """
    
    @abc.abstractclassmethod
    def from_adjacency(cls, item: graph.Adjacency) -> Composite:
        """Creates a Composite instance from an graph.Adjacency."""
        pass
    
    @abc.abstractclassmethod
    def from_edges(cls, item: graph.Edges) -> Composite:
        """Creates a Composite instance from an graph.Edges."""
        pass
    
    @abc.abstractclassmethod
    def from_matrix(cls, item: graph.Matrix) -> Composite:
        """Creates a Composite instance from a graph.Matrix."""
        pass
    
    @abc.abstractclassmethod
    def from_pipeline(cls, item: manifest.Pipeline) -> Composite:
        """Creates a Composite instance from a manifest.Pipeline."""
        pass
    
    @abc.abstractclassmethod
    def from_pipelines(cls, item: manifest.Pipelines) -> Composite:
        """Creates a Composite instance from a manifest.Pipelines."""
        pass

    @abc.abstractclassmethod
    def from_tree(cls, item: tree.Tree) -> Composite:
        """Creates a Composite instance from a tree.Tree."""
        pass
                 
    """ Required Subclass Methods """
    
    @abc.abstractmethod
    def add(item: proxy.Node, *args: Any, **kwargs: Any) -> None:
        """Adds 'node' to the stored composite object.
        
        Args:
            node (proxy.Node): a node to add to the stored composite object.
                
        """
        pass
    
    @abc.abstractmethod
    def append(
        self, item: Union[proxy.Node, Composite], 
        *args: Any, 
        **kwargs: Any) -> None:
        """Appends 'item' to the endpoint(s) of the stored composite object.

        Args:
            item (Union[proxy.Node, Composite]): a single Node or other Composite
                object to add to the stored composite object.
                
        """
        pass
        
    @abc.abstractmethod
    def delete(item: Any, *args: Any, **kwargs: Any) -> None:
        """Deletes node from the stored composite object.
        
        Args:
            item (Any): node or key to the a node to delete.
        
        Raises:
            KeyError: if 'item' is not in 'contents'.
            
        """
        pass
  
    @abc.abstractmethod
    def merge(item: Composite, *args: Any, **kwargs: Any) -> None:
        """Combines 'item' with the stored composite object.

        Args:
            item (Composite): another Composite object to add to the stored 
                composite object.
                
        """
        pass
    
    @abc.abstractmethod
    def prepend(
        self, 
        item: Union[proxy.Node, Composite], 
        *args: Any, 
        **kwargs: Any) -> None:
        """Prepends 'item' to the root(s) of the stored composite object.

        Args:
            item (Union[Node, Composite]): a single proxy.Node or other Composite
                object to add to the stored composite object.
                
        """
        pass
    
    @abc.abstractmethod
    def subset(
        self, 
        include: Union[Any, Sequence[Any]] = None,
        exclude: Union[Any, Sequence[Any]] = None, 
        *args: Any, 
        **kwargs: Any) -> Composite:
        """Returns a new Composite with a subset of 'contents'.
        
        Args:
            include (Union[Any, Sequence[Any]]): nodes which should be included
                in the new Composite.
            exclude (Union[Any, Sequence[Any]]): nodes which should not be 
                in the new Composite.

        Returns:
           Composite: with only nodes indicated by 'include' and 'exclude'.
           
        """
        pass
    
    @abc.abstractmethod
    def walk(
        self, 
        start: Optional[proxy.Node] = None,
        stop: Optional[proxy.Node] = None, 
        path: Optional[manifest.Pipeline] = None,
        return_pipelines: bool = True, 
        *args: Any, 
        **kwargs: Any) -> Union[manifest.Pipeline, manifest.Pipelines]:
        """Returns path in the stored composite object from 'start' to 'stop'.
        
        Args:
            start (Optional[proxy.Node]): node to start paths from. Defaults to None.
                If it is None, 'start' should be assigned to one of the roots
                of the Composite.
            stop (Optional[proxy.Node]): node to stop paths. Defaults to None. If it 
                is None, 'start' should be assigned to one of the roots of the 
                Composite.
            path (Optional[manifest.Pipeline]): a path from 'start' to 'stop'. Defaults 
                to None. This parameter is used by recursive methods for 
                determining a path.
            return_pipelines (bool): whether to return a manifest.Pipelines instance 
                (True) or a manifest.Pipeline instance (False). Defaults to True.

        Returns:
            Union[manifest.Pipeline, manifest.Pipelines]: path(s) through the Composite object. If 
                multiple paths are possible and 'return_pipelines' is False, 
                this method should return a manifest.Pipeline that includes all such 
                paths appended to each other. If multiple paths are possible and
                'return_pipelines' is True, a manifest.Pipelines instance with all of the
                paths should be returned. Defaults to True.
                            
        """
        pass
    
    """ Dunder Methods """
    
    @classmethod
    def __instancecheck__(cls, instance: object) -> bool:
        return check.is_composite(item = instance)

    def __add__(self, other: Composite) -> None:
        """Adds 'other' to the stored composite object using 'append'.

        Args:
            other (Union[composites.Composite]): another Graph, adjacency list, 
                an edge list, an adjacency matrix, or one or more nodes.
            
        """
        self.append(item = other)     
        return 

    def __radd__(self, other: Composite) -> None:
        """Adds 'other' to the stored composite object using 'prepend'.

        Args:
            other (Union[composites.Composite]): another Graph, adjacency list, 
                an edge list, an adjacency matrix, or one or more nodes.
            
        """
        self.prepend(item = other)     
        return 

    # def __str__(self) -> str:
    #     """Returns prettier str representation of the stored graph.

    #     Returns:
    #         str: a formatted str of class information and the contained graph.
            
    #     """
    #     return amos.recap.beautify(item = self, package = 'piles')  

