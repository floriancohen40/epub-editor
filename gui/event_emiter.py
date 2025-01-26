from collections.abc import Callable

class EventEmiter:
  def __init__(self):
      self._callbacks = {}
      
  def on(self, event_name: str, callback: Callable):
    if event_name not in self._callbacks:
      self._callbacks[event_name] = [callback]
    else:
      self._callbacks[event_name].append(callback)
  
  def trigger(self, event_name, **kwargs):
    if self._callbacks and event_name in self._callbacks:
      for callback in self._callbacks[event_name]:
        callback(**kwargs)