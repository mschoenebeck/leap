#!/usr/bin/env python3

from dataclasses import dataclass
from .BasePluginArgs import BasePluginArgs

@dataclass
class StateHistoryPluginArgs(BasePluginArgs):
    _pluginNamespace: str="eosio"
    _pluginName: str="state_history_plugin"
    stateHistoryDir: str=None
    _stateHistoryDirNodeosDefault: str='"state-history"'
    _stateHistoryDirNodeosArg: str="--state-history-dir"
    traceHistory: bool=None
    _traceHistoryNodeosDefault: bool=False
    _traceHistoryNodeosArg: str="--trace-history"
    chainStateHistory: bool=None
    _chainStateHistoryNodeosDefault: bool=False
    _chainStateHistoryNodeosArg: str="--chain-state-history"
    stateHistoryEndpoint: str=None
    _stateHistoryEndpointNodeosDefault: str="127.0.0.1:8080"
    _stateHistoryEndpointNodeosArg: str="--state-history-endpoint"
    stateHistoryUnixSocketPath: str=None
    _stateHistoryUnixSocketPathNodeosDefault: str=None
    _stateHistoryUnixSocketPathNodeosArg: str="--state-history-unix-socket-path"
    traceHistoryDebugMode: bool=None
    _traceHistoryDebugModeNodeosDefault: bool=False
    _traceHistoryDebugModeNodeosArg: str="--trace-history-debug-mode"
    stateHistoryLogRetainBlocks: int=None
    _stateHistoryLogRetainBlocksNodeosDefault: int=None
    _stateHistoryLogRetainBlocksNodeosArg: str="--state-history-log-retain-blocks"
    deleteStateHistory: bool=None
    _deleteStateHistoryNodeosDefault: bool=False
    _deleteStateHistoryNodeosArg: str="--delete-state-history"

def main():
    pluginArgs = StateHistoryPluginArgs()
    print(pluginArgs.supportedNodeosArgs())
    exit(0)

if __name__ == '__main__':
    main()
