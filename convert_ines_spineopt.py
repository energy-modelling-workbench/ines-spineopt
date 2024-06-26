def spineopt_template():
	# load json instead?
    spineopttemplate = {
		"object_parameters" : [
			["commodity", "commodity_lodf_tolerance", 0.1, None, "The minimum absolute value of the line outage distribution factor (LODF) that is considered meaningful."],
			["commodity", "commodity_physics", "commodity_physics_none", "commodity_physics_list", "Defines if the `commodity` follows lodf or ptdf physics."],
			["commodity", "commodity_physics_duration", None, None, "For how long the `commodity_physics` should apply relative to the start of the window."],
			["commodity", "commodity_ptdf_threshold", 0.001, None, "The minimum absolute value of the power transfer distribution factor (PTDF) that is considered meaningful."],
			["commodity", "mp_min_res_gen_to_demand_ratio", None, None, "Minimum ratio of renewable generation to demand for this commodity - used in the minimum renewable generation constraint within the Benders master problem"],
			["commodity", "mp_min_res_gen_to_demand_ratio_slack_penalty", None, None, "Penalty for violating the minimum renewable generation to demand ratio."],
			["commodity", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["connection", "candidate_connections", None, None, "The number of connections that may be invested in"],
			["connection", "benders_starting_connections_invested", None, None, "Fixes the number of connections invested during the first Benders iteration"],
			["connection", "forced_availability_factor", None, None, "Availability factor due to outages/deratings."],
			["connection", "connection_availability_factor", 1.0, None, "Availability of the `connection`, acting as a multiplier on its `connection_capacity`. Typically between 0-1."],
			["connection", "connection_contingency", None, "boolean_value_list", "A boolean flag for defining a contingency `connection`."],
			["connection", "connection_investment_cost", None, None, "The per unit investment cost for the connection over the `connection_investment_lifetime`"],
			["connection", "connection_investment_lifetime", None, None, "Determines the minimum investment lifetime of a connection. Once invested, it remains in service for this long"],
			["connection", "connection_investment_variable_type", "variable_type_integer", "variable_type_list", "Determines whether the investment variable is integer `variable_type_integer` or continuous `variable_type_continuous`"],
			["connection", "connection_monitored", False, "boolean_value_list", "A boolean flag for defining a contingency `connection`."],
			["connection", "connection_reactance", None, None, "The per unit reactance of a `connection`."],
			["connection", "connection_reactance_base", 1, None, "If the reactance is given for a p.u.  (e.g. p.u. = 100MW), the `connection_reactance_base` can be set to perform this conversion (e.g. *100)."],
			["connection", "connection_resistance", None, None, "The per unit resistance of a `connection`."],
			["connection", "connection_type", "connection_type_normal", "connection_type_list", "A selector between a normal and a lossless bidirectional `connection`."],
			["connection", "fix_connections_invested", None, None, "Setting a value fixes the connections_invested variable accordingly"],
			["connection", "fix_connections_invested_available", None, None, "Setting a value fixes the connections_invested_available variable accordingly"],
			["connection", "initial_connections_invested", None, None, "Setting a value fixes the connections_invested variable at the beginning"],
			["connection", "initial_connections_invested_available", None, None, "Setting a value fixes the connections_invested_available variable at the beginning"],
			["connection", "graph_view_position", None, None, "An optional setting for tweaking the position of the different elements when drawing them via Spine Toolbox Graph View."],
			["connection", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["connection", "has_binary_gas_flow", False, "boolean_value_list", "This parameter needs to be set to `True` in order to represent bidirectional pressure drive gas transfer."],
			["connection", "connections_invested_big_m_mga", None, None, "big_m_mga should be chosen as small as possible but sufficiently large. For units_invested_mga an appropriate big_m_mga would be twice the candidate connections."],
			["connection", "connections_invested_mga", False, "boolean_value_list", "Defines whether a certain variable (here: connections_invested) will be considered in the maximal-differences of the mga objective"],
			["connection", "connections_invested_mga_weight", 1, None, "Used to scale mga variables. For weightd sum mga method, the length of this weight given as an Array will determine the number of iterations."],
			["investment_group", "equal_investments", False, "boolean_value_list", "Whether all entities in the group must have the same investment decision."],
			["investment_group", "minimum_entities_invested_available", None, None, "Lower bound on the number of entities invested available in the group at any point in time."],
			["investment_group", "maximum_entities_invested_available", None, None, "Upper bound on the number of entities invested available in the group at any point in time."],
			["investment_group", "minimum_capacity_invested_available", None, None, "Lower bound on the capacity invested available in the group at any point in time."],
			["investment_group", "maximum_capacity_invested_available", None, None, "Upper bound on the capacity invested available in the group at any point in time."],
			["model", "duration_unit", "hour", "duration_unit_list", "Defines the base temporal unit of the `model`. Currently supported values are either an `hour` or a `minute`."],
			["model", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["model", "max_gap", 0.05, None, "Specifies the maximum optimality gap for the model. Currently only used for the master problem within a decomposed structure"],
			["model", "min_iterations", 1.0, None, "Specifies the minimum number of iterations for the model. Currently only used for the master problem within a decomposed structure"],
			["model", "max_iterations", 10.0, None, "Specifies the maximum number of iterations for the model. Currently only used for the master problem within a decomposed structure"],
			["model", "max_mga_iterations", None, None, "Define the number of mga iterations, i.e. how many alternative solutions will be generated."],
			["model", "max_mga_slack", 0.05, None, "Defines the maximum slack by which the alternative solution may differ from the original solution (e.g. 5% more than initial objective function value)"],
			["model", "model_end", {"data" : "2000-01-02T00:00:00", "type" : "date_time"}, None, "Defines the last timestamp to be modelled. Rolling optimization terminates after passing this point."],
			["model", "model_start", {"data" : "2000-01-01T00:00:00", "type" : "date_time"}, None, "Defines the first timestamp to be modelled. Relative `temporal_blocks` refer to this value for their start and end."],
			["model", "model_type", "spineopt_standard", "model_type_list", "Used to identify model objects as relating to the master problem or operational sub problems (default)"],
			["model", "roll_forward", None, None, "Defines how much the model moves ahead in time between solves in a rolling optimization. Without this parameter, everything is solved in as a single optimization."],
			["model", "write_lodf_file", False, "boolean_value_list", "A boolean flag for whether the LODF values should be written to a results file."],
			["model", "write_mps_file", None, "write_mps_file_list", "A selector for writing an .mps file of the model."],
			["model", "write_ptdf_file", False, "boolean_value_list", "A boolean flag for whether the LODF values should be written to a results file."],
			["model", "big_m", 1000000, None, "Sufficiently large number used for linearization bilinear terms, e.g. to enforce bidirectional flow for gas pipielines"],
			["model", "db_lp_solver", "HiGHS.jl", "db_lp_solver_list", "Solver for MIP problems. Solver package must be added and pre-configured in Julia. Overrides lp_solver RunSpineOpt kwarg"],
			["model", "db_mip_solver", "HiGHS.jl", "db_mip_solver_list", "Solver for MIP problems. Solver package must be added and pre-configured in Julia. Overrides mip_solver RunSpineOpt kwarg"],
			["model", "db_mip_solver_options", {"data" : [["HiGHS.jl", {"data" : [["presolve", "on"], ["mip_rel_gap", 0.01], ["threads", 0.0], ["time_limit", 300.01]], "type" : "map", "index_type" : "str"}], ["Cbc.jl", {"data" : [["ratioGap", 0.01], ["logLevel", 0.0]], "type" : "map", "index_type" : "str"}], ["CPLEX.jl", {"data" : [["CPX_PARAM_EPGAP", 0.01]], "type" : "map", "index_type" : "str"}]], "type" : "map", "index_type" : "str"}, None, "Map parameter containing MIP solver option name option value pairs for MIP. See solver documentation for supported solver options"],
			["model", "db_lp_solver_options", {"data" : [["HiGHS.jl", {"data" : [["presolve", "on"], ["time_limit", 300.01]], "type" : "map", "index_type" : "str"}], ["Clp.jl", {"data" : [["LogLevel", 0.0]], "type" : "map", "index_type" : "str"}]], "type" : "map", "index_type" : "str"}, None, "Map parameter containing LP solver option name option value pairs. See solver documentation for supported solver options"],
			["model", "window_duration", None, None, "The duration of the window in case it differs from roll_forward"],
			["model", "window_weight", 1, None, "The weight of the window in the rolling subproblem"], ["node", "balance_type", "balance_type_node", "balance_type_list", "A selector for how the `:nodal_balance` constraint should be handled."],
			["node", "candidate_storages", None, None, "Determines the maximum number of new storages which may be invested in"],
			["node", "benders_starting_storages_invested", None, None, "Fixes the number of storages invested during the first Benders iteration"],
			["node", "demand", 0.0, None, "Demand for the `commodity` of a `node`. Energy gains can be represented using negative `demand`."],
			["node", "downward_reserve", False, None, "Identifier for `node`s providing downward reserves"],
			["node", "fix_node_state", None, None, "Fixes the corresponding `node_state` variable to the provided value. Can be used for e.g. fixing boundary conditions."],
			["node", "fix_storages_invested", None, None, "Used to fix the value of the storages_invested variable"],
			["node", "fix_storages_invested_available", None, None, "Used to fix the value of the storages_invested_available variable"], ["node", "fix_node_pressure", None, None, "Fixes the corresponding `node_pressure` variable to the provided value"],
			["node", "fix_node_voltage_angle", None, None, "Fixes the corresponding `node_voltage_angle` variable to the provided value"], ["node", "initial_node_state", None, None, "Initializes the corresponding `node_state` variable to the provided value."],
			["node", "initial_storages_invested", None, None, "Used to initialze the value of the storages_invested variable"],
			["node", "initial_storages_invested_available", None, None, "Used to initialze the value of the storages_invested_available variable"],
			["node", "initial_node_pressure", None, None, "Initializes the corresponding `node_pressure` variable to the provided value"],
			["node", "initial_node_voltage_angle", None, None, "Initializes the corresponding `node_voltage_angle` variable to the provided value"],
			["node", "frac_state_loss", 0.0, None, "Self-discharge coefficient for `node_state` variables. Effectively, represents the *loss power per unit of state*."],
			["node", "fractional_demand", 0.0, None, "The fraction of a `node` group's `demand` applied for the `node` in question."],
			["node", "graph_view_position", None, None, "An optional setting for tweaking the position of the different elements when drawing them via Spine Toolbox Graph View."],
			["node", "has_state", False, "boolean_value_list", "A boolean flag for whether a `node` has a `node_state` variable."],
			["node", "has_pressure", False, "boolean_value_list", "A boolean flag for whether a `node` has a `node_pressure` variable."], ["node", "has_voltage_angle", False, "boolean_value_list", "A boolean flag for whether a `node` has a `node_voltage_angle` variable."],
			["node", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["node", "is_reserve_node", False, "boolean_value_list", "A boolean flag for whether a `node` is acting as a `reserve_node`"], ["node", "is_non_spinning", False, "boolean_value_list", "A boolean flag for whether a `node` is acting as a non-spinning reserve"],
			["node", "minimum_reserve_activation_time", None, None, "Duration a certain reserve product needs to be online/available"],
			["node", "nodal_balance_sense", "==", "constraint_sense_list", "A selector for `nodal_balance` constraint sense."],
			["node", "node_opf_type", "node_opf_type_normal", "node_opf_type_list", "A selector for the reference `node` (slack bus) when PTDF-based DC load-flow is enabled."],
			["node", "node_slack_penalty", None, None, "A penalty cost for `node_slack_pos` and `node_slack_neg` variables. The slack variables won't be included in the model unless there's a cost defined for them."],
			["node", "node_state_cap", None, None, "The maximum permitted value for a `node_state` variable."],
			["node", "node_state_min", 0.0, None, "The minimum permitted value for a `node_state` variable."],
			["node", "state_coeff", 1.0, None, "Represents the `commodity` content of a `node_state` variable in respect to the `unit_flow` and `connection_flow` variables. Essentially, acts as a coefficient on the `node_state` variable in the `:node_injection` constraint."],
			["node", "storage_investment_cost", None, None, "Determines the investment cost per unit state_cap over the investment life of a storage"],
			["node", "storage_investment_lifetime", None, None, "Minimum lifetime for storage investment decisions."],
			["node", "storage_investment_variable_type", "variable_type_integer", "variable_type_list", "Determines whether the storage investment variable is continuous (usually representing capacity) or integer (representing discrete units invested)"],
			["node", "tax_in_unit_flow", None, None, "Tax costs for incoming `unit_flows` on this `node`. E.g. EUR/MWh."],
			["node", "tax_net_unit_flow", None, None, "Tax costs for net incoming and outgoing `unit_flows` on this `node`. Incoming flows accrue positive net taxes, and outgoing flows accrue negative net taxes."],
			["node", "tax_out_unit_flow", None, None, "Tax costs for outgoing `unit_flows` from this `node`. E.g. EUR/MWh."],
			["node", "upward_reserve", False, None, "Identifier for `node`s providing upward reserves"],
			["node", "max_node_pressure", None, None, "Maximum allowed gas pressure at `node`."],
			["node", "min_node_pressure", None, None, "Minimum allowed gas pressure at `node`."], ["node", "max_voltage_angle", None, None, "Maximum allowed voltage angle at `node`."],
			["node", "min_voltage_angle", None, None, "Minimum allowed voltage angle at `node`. "],
			["node", "storages_invested_big_m_mga", None, None, "big_m_mga should be chosen as small as possible but sufficiently large. For units_invested_mga an appropriate big_m_mga would be twice the candidate storages."],
			["node", "storages_invested_mga", False, "boolean_value_list", "Defines whether a certain variable (here: storages_invested) will be considered in the maximal-differences of the mga objective"],
			["node", "storages_invested_mga_weight", 1, None, "Used to scale mga variables. For weighted-sum mga method, the length of this weight given as an Array will determine the number of iterations."],
			["output", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["output", "output_resolution", None, None, "Temporal resolution of the output variables associated with this `output`."], ["report", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["report", "output_db_url", None, None, "Database url for SpineOpt output."], ["settings", "version", 11, None, "Current version of the SpineOpt data structure. Modify it at your own risk (but please don't)."],
			["stochastic_scenario", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["stochastic_structure", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["temporal_block", "block_end", None, None, "The end time for the `temporal_block`. Can be given either as a `DateTime` for a static end point, or as a `Duration` for an end point relative to the start of the current optimization."],
			["temporal_block", "block_start", None, None, "The start time for the `temporal_block`. Can be given either as a `DateTime` for a static start point, or as a `Duration` for an start point relative to the start of the current optimization."],
			["temporal_block", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["temporal_block", "resolution", {"data" : "1h", "type" : "duration"}, None, "Temporal resolution of the `temporal_block`. Essentially, divides the period between `block_start` and `block_end` into `TimeSlices` with the input `resolution`."],
			["temporal_block", "weight", 1.0, None, "Weighting factor of the temporal block associated with the objective function"],
			["temporal_block", "representative_periods_mapping", None, None, "Map from date time to representative temporal block name"],
			["unit", "candidate_units", None, None, "Number of units which may be additionally constructed"],
			["unit", "benders_starting_units_invested", None, None, "Fixes the number of units invested during the first Benders iteration"],
			["unit", "curtailment_cost", None, None, "Costs for curtailing generation. Essentially, accrues costs whenever `unit_flow` not operating at its maximum available capacity. E.g. EUR/MWh"],
			["unit", "fix_units_invested", None, None, "Fix the value of the `units_invested` variable."],
			["unit", "fix_units_invested_available", None, None, "Fix the value of the `units_invested_available` variable"],
			["unit", "fix_units_on", None, None, "Fix the value of the `units_on` variable."],
            ["unit", "fix_units_out_of_service", None, None, "Fix the value of the `units_out_of_service` variable."],
			["unit", "initial_units_invested", None, None, "Initialize the value of the `units_invested` variable."],
			["unit", "initial_units_invested_available", None, None, "Initialize the value of the `units_invested_available` variable"],
			["unit", "initial_units_on", None, None, "Initialize the value of the `units_on` variable."],
            ["unit", "initial_units_out_of_service", None, None, "Initialize the value of the `units_out_of_service` variable."],
			["unit", "fom_cost", None, None, "Fixed operation and maintenance costs of a `unit`. Essentially, a cost coefficient on the existing units (incl. `number_of_units` and `units_invested_available`) and `unit_capacity` parameters. E.g. EUR/MWh"],
			["unit", "graph_view_position", None, None, "An optional setting for tweaking the position of the different elements when drawing them via Spine Toolbox Graph View."],
			["unit", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["unit", "min_down_time", None, None, "Minimum downtime of a `unit` after it shuts down."],
			["unit", "min_up_time", None, None, "Minimum uptime of a `unit` after it starts up."],
			["unit", "number_of_units", 1.0, None, "Denotes the number of 'sub units' aggregated to form the modelled `unit`."],
			["unit", "online_variable_type", "unit_online_variable_type_linear", "unit_online_variable_type_list", "A selector for how the `units_on` variable is represented within the model."],
			["unit", "shut_down_cost", None, None, "Costs of shutting down a 'sub unit', e.g. EUR/shutdown."],
			["unit", "start_up_cost", None, None, "Costs of starting up a 'sub unit', e.g. EUR/startup."],
			["unit", "forced_availability_factor", None, None, "Availability factor due to outages/deratings."],
			["unit", "unit_availability_factor", 1.0, None, "Availability of the `unit`, acting as a multiplier on its `unit_capacity`. Typically between 0-1."],
			["unit", "unit_investment_cost", None, None, "Investment cost per 'sub unit' built."], ["unit", "unit_investment_lifetime", None, None, "Minimum lifetime for unit investment decisions."],
			["unit", "unit_investment_variable_type", "unit_investment_variable_type_continuous", "unit_investment_variable_type_list", "Determines whether investment variable is integer or continuous."],
			["unit", "units_on_non_anticipativity_time", None, None, "Period of time where the value of the `units_on` variable has to be fixed to the result from the previous window."],
			["unit", "units_on_non_anticipativity_margin", None, None, "Margin by which `units_on` variable can differ from the value in the previous window during `non_anticipativity_time`."],
			["unit", "units_on_cost", None, None, "Objective function coefficient on `units_on`. An idling cost, for example"],
			["unit", "units_invested_big_m_mga", None, None, "big_m_mga should be chosen as small as possible but sufficiently large. For units_invested_mga an appropriate big_m_mga would be twice the candidate units."],
			["unit", "units_invested_mga", False, "boolean_value_list", "Defines whether a certain variable (here: units_invested) will be considered in the maximal-differences of the mga objective"],
			["unit", "units_invested_mga_weight", 1, None, "Used to scale mga variables. For weightd sum mga method, the length of this weight given as an Array will determine the number of iterations."],
			["unit", "is_renewable", False, "boolean_value_list", "Whether the unit is renewable - used in the minimum renewable generation constraint within the Benders master problem"],
            ["unit", "scheduled_outage_duration", None, None, "Specifies the amount of time a unit must be out of service for maintenance as a single block over the course of the optimisation window"],
			["unit", "outage_variable_type", "unit_online_variable_type_none", "unit_online_variable_type_list", "Determines whether the outage variable is integer or continuous or none(no optimisation of maintenance outages)."],
			["unit", "units_unavailable", 0, None, "Represents the number of units out of service"],
			["user_constraint", "constraint_sense", "==", "constraint_sense_list", "A selector for the sense of the `user_constraint`."],
			["user_constraint", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["user_constraint", "right_hand_side", 0.0, None, "The right-hand side, constant term in a `user_constraint`. Can be time-dependent and used e.g. for complicated efficiency approximations."],
			["user_constraint", "user_constraint_slack_penalty", None, None, "A penalty for violating a user constraint."]
		],
		"relationship_parameters" : [
			["connection__from_node", "connection_capacity", None, None, "Limits the `connection_flow` variable from the `from_node`. `from_node` can be a group of `nodes`, in which case the sum of the `connection_flow` is constrained."],
			["connection__from_node", "connection_conv_cap_to_flow", 1.0, None, "Optional coefficient for `connection_capacity` unit conversions in the case that the `connection_capacity` value is incompatible with the desired `connection_flow` units."],
			["connection__from_node", "connection_emergency_capacity", None, None, "Post contingency flow capacity of a `connection`. Sometimes referred to as emergency rating"],
			["connection__from_node", "fix_connection_flow", None, None, "Fix the value of the `connection_flow` variable."],
			["connection__from_node", "fix_binary_gas_connection_flow", None, None, "Fix the value of the `connection_flow_binary` variable, and hence pre-determine the direction of flow in the connection."],
			["connection__from_node", "fix_connection_intact_flow", None, None, "Fix the value of the `connection_intact_flow` variable."],
			["connection__from_node", "initial_connection_flow", None, None, "Initialize the value of the `connection_flow` variable."],
			["connection__from_node", "initial_binary_gas_connection_flow", None, None, "Initialize the value of the `connection_flow_binary` variable, and hence pre-determine the direction of flow in the connection."],
			["connection__from_node", "initial_connection_intact_flow", None, None, "Initialize the value of the `connection_intact_flow` variable."],
			["connection__from_node", "graph_view_position", None, None, "An optional setting for tweaking the position of the different elements when drawing them via Spine Toolbox Graph View."],
			["connection__from_node", "connection_flow_cost", None, None, "Variable costs of a flow through a `connection`. E.g. EUR/MWh of energy throughput."],
			["connection__from_node", "connection_flow_non_anticipativity_time", None, None, "Period of time where the value of the `connection_flow` variable has to be fixed to the result from the previous window."],
			["connection__from_node", "connection_flow_non_anticipativity_margin", None, None, "Margin by which `connection_flow` variable can differ from the value in the previous window during `non_anticipativity_time`."],
			["connection__from_node", "connection_intact_flow_non_anticipativity_time", None, None, "Period of time where the value of the `connection_intact_flow` variable has to be fixed to the result from the previous window."],
			["connection__from_node", "connection_intact_flow_non_anticipativity_margin", None, None, "Margin by which `connection_intact_flow` variable can differ from the value in the previous window during `non_anticipativity_time`."],
			["connection__from_node__user_constraint", "connection_flow_coefficient", 0.0, None, "defines the user constraint coefficient on the connection flow variable in the from direction"],
			["connection__node__node", "connection_flow_delay", {"data" : "0h", "type" : "duration"}, None, "Delays the `connection_flows` associated with the latter `node` in respect to the `connection_flows` associated with the first `node`."],
			["connection__node__node", "fix_ratio_out_in_connection_flow", None, None, "Fix the ratio between an outgoing `connection_flow` to the first `node` and an incoming `connection_flow` from the second `node`."],
			["connection__node__node", "max_ratio_out_in_connection_flow", None, None, "Maximum ratio between an outgoing `connection_flow` to the first `node` and an incoming `connection_flow` from the second `node`."],
			["connection__node__node", "min_ratio_out_in_connection_flow", None, None, "Minimum ratio between an outgoing `connection_flow` to the first `node` and an incoming `connection_flow` from the second `node`."],
			["connection__node__node", "fixed_pressure_constant_1", None, None, "Fixed pressure points for pipelines for the outer approximation of the Weymouth approximation. The direction of flow is the first node in the relationship to the second node in the relationship."],
			["connection__node__node", "fixed_pressure_constant_0", None, None, "Fixed pressure points for pipelines for the outer approximation of the Weymouth approximation. The direction of flow is the first node in the relationship to the second node in the relationship."],
			["connection__node__node", "compression_factor", None, None, "The compression factor establishes a compression from an origin node to a receiving node, which are connected through a connection. The first node corresponds to the origin node, the second to the (compressed) destination node. Typically the value is >=1."],
			["connection__node__node", "connection_linepack_constant", None, None, "The linepack constant is a property of gas pipelines and relates the linepack to the pressure of the adjacent nodes."],
			["connection__to_node", "connection_capacity", None, None, "Limits the `connection_flow` variable to the `to_node`. `to_node` can be a group of `nodes`, in which case the sum of the `connection_flow` is constrained."],
			["connection__to_node", "connection_conv_cap_to_flow", 1.0, None, "Optional coefficient for `connection_capacity` unit conversions in the case the `connection_capacity` value is incompatible with the desired `connection_flow` units."],
			["connection__to_node", "connection_emergency_capacity", None, None, "The maximum post-contingency flow on a monitored `connection`."],
			["connection__to_node", "fix_connection_flow", None, None, "Fix the value of the `connection_flow` variable."],
			["connection__to_node", "fix_binary_gas_connection_flow", None, None, "Fix the value of the `connection_flow_binary` variable, and hence pre-determine the direction of flow in the connection."],
			["connection__to_node", "fix_connection_intact_flow", None, None, "Fix the value of the `connection_intact_flow` variable."],
			["connection__to_node", "initial_connection_flow", None, None, "Initialize the value of the `connection_flow` variable."],
			["connection__to_node", "initial_binary_gas_connection_flow", None, None, "Initialize the value of the `connection_flow_binary` variable, and hence pre-determine the direction of flow in the connection."],
			["connection__to_node", "initial_connection_intact_flow", None, None, "Initialize the value of the `connection_intact_flow` variable."],
			["connection__to_node", "graph_view_position", None, None, "An optional setting for tweaking the position of the different elements when drawing them via Spine Toolbox Graph View."],
			["connection__to_node", "connection_flow_cost", None, None, "Variable costs of a flow through a `connection`. E.g. EUR/MWh of energy throughput."],
			["connection__to_node", "connection_flow_non_anticipativity_time", None, None, "Period of time where the value of the `connection_flow` variable has to be fixed to the result from the previous window."],
			["connection__to_node", "connection_flow_non_anticipativity_margin", None, None, "Margin by which `connection_flow` variable can differ from the value in the previous window during `non_anticipativity_time`."],
			["connection__to_node", "connection_intact_flow_non_anticipativity_time", None, None, "Period of time where the value of the `connection_intact_flow` variable has to be fixed to the result from the previous window."],
			["connection__to_node", "connection_intact_flow_non_anticipativity_margin", None, None, "Margin by which `connection_intact_flow` variable can differ from the value in the previous window during `non_anticipativity_time`."],
			["connection__to_node__user_constraint", "connection_flow_coefficient", 0.0, None, "defines the user constraint coefficient on the connection flow variable in the to direction"],
			["connection__user_constraint", "connections_invested_coefficient", 0.0, None, "coefficient of `connections_invested` in the specific `user_constraint`"],
			["connection__user_constraint", "connections_invested_available_coefficient", 0.0, None, "coefficient of `connections_invested_available` in the specific `user_constraint`"],
			["node__node", "diff_coeff", 0.0, None, "Commodity diffusion coefficient between two `nodes`. Effectively, denotes the *diffusion power per unit of state* from the first `node` to the second."],
			["node__temporal_block", "cyclic_condition", False, "boolean_value_list", "If the cyclic condition is set to True for a storage node, the `node_state` at the end of the optimization window has to be larger than or equal to the initial storage state."],
			["node__temporal_block", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["node__stochastic_structure", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["node__user_constraint", "demand_coefficient", 0.0, None, "coefficient of the specified node's demand in the specified user constraint"],
			["node__user_constraint", "node_state_coefficient", 0.0, None, "Coefficient of the specified node's state variable in the specified user constraint."],
			["node__user_constraint", "storages_invested_coefficient", 0.0, None, "Coefficient of the specified node's storage investment variable in the specified user constraint."],
			["node__user_constraint", "storages_invested_available_coefficient", 0.0, None, "Coefficient of the specified node's storages invested available variable in the specified user constraint."],
			["report__output", "overwrite_results_on_rolling", True, None, "Whether or not results from further windows should overwrite results from previous ones."],
			["stochastic_structure__stochastic_scenario", "stochastic_scenario_end", None, None, "A `Duration` for when a `stochastic_scenario` ends and its `child_stochastic_scenarios` start. Values are interpreted relative to the start of the current solve, and if no value is given, the `stochastic_scenario` is assumed to continue indefinitely."],
			["stochastic_structure__stochastic_scenario", "weight_relative_to_parents", 1.0, None, "The weight of the `stochastic_scenario` in the objective function relative to its parents."],
			["unit__commodity", "max_cum_in_unit_flow_bound", None, None, "Set a maximum cumulative upper bound for a `unit_flow`"],
			["unit__from_node", "fix_nonspin_units_started_up", None, None, "Fix the `nonspin_units_started_up` variable."],
			["unit__from_node", "fix_unit_flow", None, None, "Fix the `unit_flow` variable."],
			["unit__from_node", "fix_unit_flow_op", None, None, "Fix the `unit_flow_op` variable."],
			["unit__from_node", "initial_nonspin_units_started_up", None, None, "Initialize the `nonspin_units_started_up` variable."],
			["unit__from_node", "initial_unit_flow", None, None, "Initialize the `unit_flow` variable."],
			["unit__from_node", "initial_unit_flow_op", None, None, "Initialize the `unit_flow_op` variable."],
			["unit__from_node", "min_unit_flow", 0.0, None, "Set lower bound of the `unit_flow` variable."],
			["unit__from_node", "fuel_cost", None, None, "Variable fuel costs than can be attributed to a `unit_flow`. E.g. EUR/MWh"],
			["unit__from_node", "reserve_procurement_cost", None, None, "Procurement cost for reserves"],
			["unit__from_node", "graph_view_position", None, None, "An optional setting for tweaking the position of the different elements when drawing them via Spine Toolbox Graph View."],
			["unit__from_node", "shut_down_limit", None, None, "Max. downward ramp for units shutting down"],
			["unit__from_node", "start_up_limit", None, None, "Maximum ramp-up during startups."],
			["unit__from_node", "max_total_cumulated_unit_flow_from_node", None, None, "Bound on the maximum cumulated flows of a unit group from a node group e.g max consumption of certain commodity."],
			["unit__from_node", "min_total_cumulated_unit_flow_from_node", None, None, "Bound on the minimum cumulated flows of a unit group from a node group."],
			["unit__from_node", "minimum_operating_point", None, None, "Minimum level for the `unit_flow` relative to the `units_on` online capacity."],
			["unit__from_node", "operating_points", None, None, "Operating points for piecewise-linear `unit` efficiency approximations."],
			["unit__from_node", "ramp_down_limit", None, None, "Limit the maximum ramp-down rate of an online unit, given as a fraction of the unit_capacity. [ramp_down_limit] = %/t, e.g. 0.2/h"],
			["unit__from_node", "ramp_up_limit", None, None, "Limit the maximum ramp-up rate of an online unit, given as a fraction of the unit_capacity. [ramp_up_limit] = %/t, e.g. 0.2/h"],
			["unit__from_node", "unit_capacity", None, None, "Maximum `unit_flow` capacity of a single 'sub_unit' of the `unit`."],
			["unit__from_node", "unit_conv_cap_to_flow", 1.0, None, "Optional coefficient for `unit_capacity` unit conversions in the case the `unit_capacity` value is incompatible with the desired `unit_flow` units."],
			["unit__from_node", "vom_cost", None, None, "Variable operating costs of a `unit_flow` variable. E.g. EUR/MWh."],
			["unit__from_node", "unit_flow_non_anticipativity_time", None, None, "Period of time where the value of the `unit_flow` variable has to be fixed to the result from the previous window."],
			["unit__from_node", "unit_flow_non_anticipativity_margin", None, None, "Margin by which `unit_flow` variable can differ from the value in the previous window during `non_anticipativity_time`."],
			["unit__from_node", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["unit__from_node", "ordered_unit_flow_op", False, "boolean_value_list", "Defines whether the segments of this unit flow are ordered as per the rank of their operating points."],
			["unit__from_node__user_constraint", "graph_view_position", None, None, "An optional setting for tweaking the position of the different elements when drawing them via Spine Toolbox Graph View."],
			["unit__from_node__user_constraint", "unit_flow_coefficient", 0.0, None, "Coefficient of a `unit_flow` variable for a custom `user_constraint`."],
			["unit__node__node", "fix_ratio_in_in_unit_flow", None, None, "Fix the ratio between two `unit_flows` coming into the `unit` from the two `nodes`."],
			["unit__node__node", "fix_ratio_in_out_unit_flow", None, None, "Fix the ratio between an incoming `unit_flow` from the first `node` and an outgoing `unit_flow` to the second `node`."],
			["unit__node__node", "fix_ratio_out_in_unit_flow", None, None, "Fix the ratio between an outgoing `unit_flow` to the first `node` and an incoming `unit_flow` from the second `node`."],
			["unit__node__node", "fix_ratio_out_out_unit_flow", None, None, "Fix the ratio between two `unit_flows` going from the `unit` into the two `nodes`."],
			["unit__node__node", "fix_units_on_coefficient_in_in", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `fix_ratio_in_in_unit_flow` constraint."],
			["unit__node__node", "fix_units_on_coefficient_in_out", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `fix_ratio_in_out_unit_flow` constraint."],
			["unit__node__node", "fix_units_on_coefficient_out_in", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `fix_ratio_out_in_unit_flow` constraint."],
			["unit__node__node", "fix_units_on_coefficient_out_out", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `fix_ratio_out_out_unit_flow` constraint."],
			["unit__node__node", "max_ratio_in_in_unit_flow", None, None, "Maximum ratio between two `unit_flows` coming into the `unit` from the two `nodes`."],
			["unit__node__node", "max_ratio_in_out_unit_flow", None, None, "Maximum ratio between an incoming `unit_flow` from the first `node` and an outgoing `unit_flow` to the second `node`."],
			["unit__node__node", "max_ratio_out_in_unit_flow", None, None, "Maximum ratio between an outgoing `unit_flow` to the first `node` and an incoming `unit_flow` from the second `node`."],
			["unit__node__node", "max_ratio_out_out_unit_flow", None, None, "Maximum ratio between two `unit_flows` going from the `unit` into the two `nodes`."],
			["unit__node__node", "max_units_on_coefficient_in_in", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `max_ratio_in_in_unit_flow` constraint."],
			["unit__node__node", "max_units_on_coefficient_in_out", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `max_ratio_in_out_unit_flow` constraint."],
			["unit__node__node", "max_units_on_coefficient_out_in", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `max_ratio_out_in_unit_flow` constraint."],
			["unit__node__node", "max_units_on_coefficient_out_out", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `max_ratio_out_out_unit_flow` constraint."],
			["unit__node__node", "min_ratio_in_in_unit_flow", None, None, "Minimum ratio between two `unit_flows` coming into the `unit` from the two `nodes`."],
			["unit__node__node", "min_ratio_in_out_unit_flow", None, None, "Minimum ratio between an incoming `unit_flow` from the first `node` and an outgoing `unit_flow` to the second `node`."],
			["unit__node__node", "min_ratio_out_in_unit_flow", None, None, "Minimum ratio between an outgoing `unit_flow` to the first `node` and an incoming `unit_flow` from the second `node`."],
			["unit__node__node", "min_ratio_out_out_unit_flow", None, None, "Minimum ratio between two `unit_flows` going from the `unit` into the two `nodes`."],
			["unit__node__node", "min_units_on_coefficient_in_in", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `min_ratio_in_in_unit_flow` constraint."],
			["unit__node__node", "min_units_on_coefficient_in_out", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `min_ratio_in_out_unit_flow` constraint."],
			["unit__node__node", "min_units_on_coefficient_out_in", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `min_ratio_out_in_unit_flow` constraint."],
			["unit__node__node", "min_units_on_coefficient_out_out", 0.0, None, "Optional coefficient for the `units_on` variable impacting the `min_ratio_out_out_unit_flow` constraint."],
			["unit__node__node", "unit_incremental_heat_rate", None, None, "Standard piecewise incremental heat rate where node1 is assumed to be the fuel and node2 is assumed to be electriciy. Assumed monotonically increasing. Array type or single coefficient where the number of coefficients must match the dimensions of `unit_operating_points`"],
			["unit__node__node", "unit_idle_heat_rate", 0.0, None, "Flow from node1 per unit time and per `units_on` that results in no additional flow to node2"],
			["unit__node__node", "unit_start_flow", 0.0, None, "Flow from node1 that is incurred when a unit is started up."],
			["unit__to_node", "fix_nonspin_units_shut_down", None, None, "Fix the `nonspin_units_shut_down` variable."],
			["unit__to_node", "fix_nonspin_units_started_up", None, None, "Fix the `nonspin_units_started_up` variable."],
			["unit__to_node", "fix_unit_flow", None, None, "Fix the `unit_flow` variable."],
			["unit__to_node", "fix_unit_flow_op", None, None, "Fix the `unit_flow_op` variable."],
			["unit__to_node", "initial_nonspin_units_shut_down", None, None, "Initialize the `nonspin_units_shut_down` variable."],
			["unit__to_node", "initial_nonspin_units_started_up", None, None, "Initialize the `nonspin_units_started_up` variable."],
			["unit__to_node", "initial_unit_flow", None, None, "Initialize the `unit_flow` variable."],
			["unit__to_node", "initial_unit_flow_op", None, None, "Initialize the `unit_flow_op` variable."],
			["unit__to_node", "min_unit_flow", 0.0, None, "Set lower bound of the `unit_flow` variable."],
			["unit__to_node", "fuel_cost", None, None, "Variable fuel costs than can be attributed to a `unit_flow`. E.g. EUR/MWh"],
			["unit__to_node", "reserve_procurement_cost", None, None, "Procurement cost for reserves"],
			["unit__to_node", "graph_view_position", None, None, "An optional setting for tweaking the position of the different elements when drawing them via Spine Toolbox Graph View."],
			["unit__to_node", "shut_down_limit", None, None, "Maximum ramp-down during shutdowns"],
			["unit__to_node", "start_up_limit", None, None, "Maximum ramp-up during startups"],
			["unit__to_node", "max_total_cumulated_unit_flow_to_node", None, None, "Bound on the maximum cumulated flows of a unit group to a node group, e.g. total GHG emissions."],
			["unit__to_node", "min_total_cumulated_unit_flow_to_node", None, None, "Bound on the minimum cumulated flows of a unit group to a node group, e.g. total renewable production."],
			["unit__to_node", "minimum_operating_point", None, None, "Minimum level for the `unit_flow` relative to the `units_on` online capacity."],
			["unit__to_node", "operating_points", None, None, "Decomposes the flow variable into a number of separate operating segment variables. Used to in conjunction with `unit_incremental_heat_rate` and/or `user_constraint`s"],
			["unit__to_node", "ramp_down_limit", None, None, "Limit the maximum ramp-down rate of an online unit, given as a fraction of the unit_capacity. [ramp_down_limit] = %/t, e.g. 0.2/h"],
			["unit__to_node", "ramp_up_limit", None, None, "Limit the maximum ramp-up rate of an online unit, given as a fraction of the unit_capacity. [ramp_up_limit] = %/t, e.g. 0.2/h"],
			["unit__to_node", "unit_capacity", None, None, "Maximum `unit_flow` capacity of a single 'sub_unit' of the `unit`."],
			["unit__to_node", "unit_conv_cap_to_flow", 1.0, None, "Optional coefficient for `unit_capacity` unit conversions in the case the `unit_capacity` value is incompatible with the desired `unit_flow` units."], ["unit__to_node", "vom_cost", None, None, "Variable operating costs of a `unit_flow` variable. E.g. EUR/MWh."],
			["unit__to_node", "unit_flow_non_anticipativity_time", None, None, "Period of time where the value of the `unit_flow` variable has to be fixed to the result from the previous window."],
			["unit__to_node", "unit_flow_non_anticipativity_margin", None, None, "Margin by which `unit_flow` variable can differ from the value in the previous window during `non_anticipativity_time`."],
			["unit__to_node", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["unit__to_node", "ordered_unit_flow_op", False, "boolean_value_list", "Defines whether the segments of this unit flow are ordered as per the rank of their operating points."],
			["unit__to_node__user_constraint", "graph_view_position", None, None, "An optional setting for tweaking the position of the different elements when drawing them via Spine Toolbox Graph View."],
			["unit__to_node__user_constraint", "unit_flow_coefficient", 0.0, None, "Coefficient of a `unit_flow` variable for a custom `user_constraint`."],
			["unit__user_constraint", "units_on_coefficient", 0.0, None, "Coefficient of a `units_on` variable for a custom `user_constraint`."],
			["unit__user_constraint", "units_started_up_coefficient", 0.0, None, "Coefficient of a `units_started_up` variable for a custom `user_constraint`."],
			["unit__user_constraint", "units_invested_coefficient", 0.0, None, "Coefficient of the `units_invested` variable in the specified `user_constraint`."],
			["unit__user_constraint", "units_invested_available_coefficient", 0.0, None, "Coefficient of the `units_invested_available` variable in the specified `user_constraint`."],
			["units_on__stochastic_structure", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"],
			["units_on__temporal_block", "is_active", True, "boolean_value_list", "If False, the object is excluded from the model if the tool filter object activity control is specified"]
		],
		"tool_features" : [
			["object_activity_control", "commodity", "is_active", False],
			["object_activity_control", "connection", "is_active", False],
			["object_activity_control", "model", "is_active", False],
			["object_activity_control", "node", "is_active", False],
			["object_activity_control", "output", "is_active", False],
			["object_activity_control", "report", "is_active", False],
			["object_activity_control", "stochastic_scenario", "is_active", False],
			["object_activity_control", "stochastic_structure", "is_active", False],
			["object_activity_control", "temporal_block", "is_active", False],
			["object_activity_control", "unit", "is_active", False],
			["object_activity_control", "user_constraint", "is_active", False],
			["object_activity_control", "node__stochastic_structure", "is_active", False],
			["object_activity_control", "node__temporal_block", "is_active", False],
			["object_activity_control", "unit__to_node", "is_active", False],
			["object_activity_control", "unit__from_node", "is_active", False],
			["object_activity_control", "units_on__stochastic_structure", "is_active", False],
			["object_activity_control", "units_on__temporal_block", "is_active", False]
		],
		"features" : [
			["commodity", "is_active", "boolean_value_list", "boolean_value_list"],
			["connection", "is_active", "boolean_value_list", "boolean_value_list"],
			["model", "is_active", "boolean_value_list", "boolean_value_list"],
			["node", "is_active", "boolean_value_list", "boolean_value_list"],
			["output", "is_active", "boolean_value_list", "boolean_value_list"],
			["report", "is_active", "boolean_value_list", "boolean_value_list"],
			["stochastic_scenario", "is_active", "boolean_value_list", "boolean_value_list"],
			["stochastic_structure", "is_active", "boolean_value_list", "boolean_value_list"],
			["temporal_block", "is_active", "boolean_value_list", "boolean_value_list"],
			["unit", "is_active", "boolean_value_list", "boolean_value_list"],
			["user_constraint", "is_active", "boolean_value_list", "boolean_value_list"],
			["node__stochastic_structure", "is_active", "boolean_value_list", "boolean_value_list"],
			["node__temporal_block", "is_active", "boolean_value_list", "boolean_value_list"],
			["unit__from_node", "is_active", "boolean_value_list", "boolean_value_list"],
			["unit__to_node", "is_active", "boolean_value_list", "boolean_value_list"],
			["units_on__stochastic_structure", "is_active", "boolean_value_list", "boolean_value_list"],
			["units_on__temporal_block", "is_active", "boolean_value_list", "boolean_value_list"]
		],
		"objects" : [
			["output", "binary_gas_connection_flow", None],
			["output", "connection_flow", None],
			["output", "connection_intact_flow", None],
			["output", "connections_decommissioned", None],
			["output", "connections_invested_available", None],
			["output", "connections_invested", None],
			["output", "contingency_is_binding", None],
			["output", "mp_objective_lowerbound", None],
			["output", "mga_objective", None],
			["output", "node_injection", None],
			["output", "node_pressure", None],
			["output", "node_slack_neg", None],
			["output", "node_slack_pos", None],
			["output", "node_state", None],
			["output", "node_voltage_angle", None],
			["output", "nonspin_units_shut_down", None],
			["output", "nonspin_units_started_up", None],
			["output", "storages_decommissioned", None],
			["output", "storages_invested_available", None],
			["output", "storages_invested", None], ["output", "unit_flow_op_active", None],
			["output", "unit_flow_op", None],
			["output", "unit_flow", None],
			["output", "units_available", None],
			["output", "units_invested_available", None],
			["output", "units_invested", None],
			["output", "units_mothballed", None],
			["output", "units_on", None],
			["output", "units_shut_down", None],
			["output", "units_started_up", None],
			["output", "connection_avg_throughflow", None],
			["output", "connection_avg_intact_throughflow", None],
			["output", "variable_om_costs", None],
			["output", "fixed_om_costs", None],
			["output", "taxes", None],
			["output", "fuel_costs", None],
			["output", "unit_investment_costs", None],
			["output", "connection_investment_costs", None],
			["output", "storage_investment_costs", None],
			["output", "start_up_costs", None],
			["output", "shut_down_costs", None],
			["output", "objective_penalties", None],
			["output", "connection_flow_costs", None],
			["output", "renewable_curtailment_costs", None],
			["output", "res_proc_costs", None],
			["output", "units_on_costs", None],
			["output", "total_costs", None],
			["output", "relative_optimality_gap", None]
		],
		"tools" : [
			["object_activity_control", ""]
		],
		"tool_feature_methods" : [
			["object_activity_control", "commodity", "is_active", True],
			["object_activity_control", "connection", "is_active", True],
			["object_activity_control", "model", "is_active", True],
			["object_activity_control", "node", "is_active", True],
			["object_activity_control", "output", "is_active", True],
			["object_activity_control", "report", "is_active", True],
			["object_activity_control", "stochastic_scenario", "is_active", True],
			["object_activity_control", "stochastic_structure", "is_active", True],
			["object_activity_control", "temporal_block", "is_active", True],
			["object_activity_control", "unit", "is_active", True],
			["object_activity_control", "user_constraint", "is_active", True],
			["object_activity_control", "node__stochastic_structure", "is_active", True],
			["object_activity_control", "node__temporal_block", "is_active", True],
			["object_activity_control", "unit__to_node", "is_active", True],
			["object_activity_control", "unit__from_node", "is_active", True],
			["object_activity_control", "units_on__stochastic_structure", "is_active", True],
			["object_activity_control", "units_on__temporal_block", "is_active", True]
		],
		"object_classes" : [
			["commodity", "A good or product that can be consumed, produced, traded. E.g., electricity, oil, gas, water...", 281473533932880],
			["connection", "A transfer of commodities between nodes. E.g. electricity line, gas pipeline...", 280378317271233],
			["investment_group", "A group of investments that need to be done together.", 281105609585860], ["model", "An instance of SpineOpt, that specifies general parameters such as the temporal horizon.", 281107035648412],
			["node", "A universal aggregator of commodify flows over units and connections, with storage capabilities.", 280740554077951],
			["output", "A variable name from SpineOpt that can be included in a report.", 280743406202948],
			["report", "A results report from a particular SpineOpt run, including the value of specific variables.", 281108461711708], ["settings", "Internal SpineOpt settings. We kindly advise not to mess with this one.", 280375465144798],
			["stochastic_scenario", "A scenario for stochastic optimisation in SpineOpt.", 280743389491710],
			["stochastic_structure", "A group of stochastic scenarios that represent a structure.", 281470681806146],
			["temporal_block", "A length of time with a particular resolution.", 280376891207703], ["unit", "A conversion of one/many comodities between nodes.", 281470681805429],
			["user_constraint", "A generic data-driven custom constraint.", 281473533931636]
		],
		"relationship_classes" : [
			["connection__from_node", ["connection", "node"], "Defines the `nodes` the `connection` can take input from, and holds most `connection_flow` variable specific parameters.", 280378317271897],
			["connection__from_node__investment_group", ["connection", "node", "investment_group"], "Indicates which connection capacities are included in the capacity invested available of an investment group"],
			["connection__from_node__user_constraint", ["connection", "node", "user_constraint"], "when specified this relationship allows the relevant flow connection flow variable to be included in the specified user constraint"],
			["connection__investment_group", ["connection", "investment_group"], "Indicates that a `connection` belongs in an `investment_group`."],
			["connection__investment_stochastic_structure", ["connection", "stochastic_structure"], "Defines the stochastic structure of the connections investments variable"],
			["connection__investment_temporal_block", ["connection", "temporal_block"], "Defines the temporal resolution of the connections investments variable"],
			["connection__node__node", ["connection", "node", "node"], "Holds parameters spanning multiple `connection_flow` variables to and from multiple `nodes`."],
			["connection__to_node__investment_group", ["connection", "node", "investment_group"], "Indicates which connection capacities are included in the capacity invested available of an investment group"],
			["connection__to_node", ["connection", "node"], "Defines the `nodes` the `connection` can output to, and holds most `connection_flow` variable specific parameters.", 280378317271898],
			["connection__to_node__user_constraint", ["connection", "node", "user_constraint"], "when specified this relationship allows the relevant flow connection flow variable to be included in the specified user constraint"],
			["connection__user_constraint", ["connection", "user_constraint"], "Relationship required to involve a connections investment variables in a user_constraint"],
			["model__default_investment_stochastic_structure", ["model", "stochastic_structure"], "Defines the default stochastic structure used for investment variables, which will be replaced by more specific definitions"],
			["model__default_investment_temporal_block", ["model", "temporal_block"], "Defines the default temporal block used for investment variables, which will be replaced by more specific definitions"],
			["model__default_stochastic_structure", ["model", "stochastic_structure"], "Defines the default stochastic structure used for model variables, which will be replaced by more specific definitions"],
			["model__default_temporal_block", ["model", "temporal_block"], "Defines the default temporal block used for model variables, which will be replaced by more specific definitions"],
			["model__report", ["model", "report"], "Determines which reports are written for each model and in turn, which outputs are written for each model"],
			["node__commodity", ["node", "commodity"], "Define a `commodity` for a `node`. Only a single `commodity` is permitted per `node`"],
			["node__investment_group", ["node", "investment_group"], "Indicates that a `node` belongs in a `investment_group`."],
			["node__investment_stochastic_structure", ["node", "stochastic_structure"], "defines the stochastic structure for node related investments, currently only storages"],
			["node__investment_temporal_block", ["node", "temporal_block"], "defines the temporal resolution for node related investments, currently only storages"],
			["node__node", ["node", "node"], "Holds parameters for direct interactions between two `nodes`, e.g. `node_state` diffusion coefficients."],
			["node__stochastic_structure", ["node", "stochastic_structure"], "Defines which specific `stochastic_structure` is used by the `node` and all `flow` variables associated with it. Only one `stochastic_structure` is permitted per `node`."],
			["node__temporal_block", ["node", "temporal_block"], "Defines the `temporal_blocks` used by the `node` and all the `flow` variables associated with it."],
			["node__user_constraint", ["node", "user_constraint"], "specifying this relationship allows a node's demand or node_state to be included in the specified user constraint"],
			["parent_stochastic_scenario__child_stochastic_scenario", ["stochastic_scenario", "stochastic_scenario"], "Defines the master stochastic direct acyclic graph, meaning how the `stochastic_scenarios` are related to each other."],
			["report__output", ["report", "output"], "Output object related to a report object are returned to the output database (if they appear in the model as variables)"],
			["stochastic_structure__stochastic_scenario", ["stochastic_structure", "stochastic_scenario"], "Defines which `stochastic_scenarios` are included in which `stochastic_structure`, and holds the parameters required for realizing the structure in combination with the `temporal_blocks`."],
			["unit__commodity", ["unit", "commodity"], "Holds parameters for `commodities` used by the `unit`."],
			["unit__from_node", ["unit", "node"], "Defines the `nodes` the `unit` can take input from, and holds most `unit_flow` variable specific parameters.", 281470681805657],
			["unit__from_node__investment_group", ["unit", "node", "investment_group"], "Indicates which unit capacities are included in the capacity invested available of an investment group"],
			["unit__from_node__user_constraint", ["unit", "node", "user_constraint"], "Defines which input `unit_flows` are included in the `user_constraint`, and holds their parameters."],
			["unit__investment_group", ["unit", "investment_group"], "Indicates that a `unit` belongs in an `investment_group`."],
			["unit__investment_stochastic_structure", ["unit", "stochastic_structure"], "Sets the stochastic structure for investment decisions - overrides `model__default_investment_stochastic_structure`."],
			["unit__investment_temporal_block", ["unit", "temporal_block"], "Sets the temporal resolution of investment decisions - overrides `model__default_investment_temporal_block`"],
			["unit__node__node", ["unit", "node", "node"], "Holds parameters spanning multiple `unit_flow` variables to and from multiple `nodes`."],
			["unit__to_node", ["unit", "node"], "Defines the `nodes` the `unit` can output to, and holds most `unit_flow` variable specific parameters.", 281470681805658],
			["unit__to_node__investment_group", ["unit", "node", "investment_group"], "Indicates which unit capacities are included in the capacity invested available of an investment group"],
			["unit__to_node__user_constraint", ["unit", "node", "user_constraint"], "Defines which output `unit_flows` are included in the `user_constraint`, and holds their parameters."],
			["unit__user_constraint", ["unit", "user_constraint"], "Defines which `units_on` variables are included in the `user_constraint`, and holds their parameters."],
			["units_on__stochastic_structure", ["unit", "stochastic_structure"], "Defines which specific `stochastic_structure` is used for the `units_on` variable of the `unit`. Only one `stochastic_structure` is permitted per `unit`."],
			["units_on__temporal_block", ["unit", "temporal_block"], "Defines which specific `temporal_blocks` are used by the `units_on` variable of the `unit`."]
		],
		"parameter_value_lists" : [
			["balance_type_list", "balance_type_group"],
			["balance_type_list", "balance_type_node"],
			["balance_type_list", "balance_type_none"],
			["boolean_value_list", False],
			["boolean_value_list", True],
			["commodity_physics_list", "commodity_physics_lodf"],
			["commodity_physics_list", "commodity_physics_none"],
			["commodity_physics_list", "commodity_physics_ptdf"],
			["connection_investment_variable_type_list", "connection_investment_variable_type_continuous"],
			["connection_investment_variable_type_list", "connection_investment_variable_type_integer"],
			["connection_type_list", "connection_type_lossless_bidirectional"],
			["connection_type_list", "connection_type_normal"],
			["constraint_sense_list", "<="],
			["constraint_sense_list", "=="],
			["constraint_sense_list", ">="],
			["duration_unit_list", "hour"],
			["duration_unit_list", "minute"],
			["model_type_list", "spineopt_benders"],
			["model_type_list", "spineopt_standard"],
			["model_type_list", "spineopt_other"],
			["model_type_list", "spineopt_mga"],
			["node_opf_type_list", "node_opf_type_normal"],
			["node_opf_type_list", "node_opf_type_reference"],
			["unit_investment_variable_type_list", "unit_investment_variable_type_continuous"],
			["unit_investment_variable_type_list", "unit_investment_variable_type_integer"],
			["unit_online_variable_type_list", "unit_online_variable_type_binary"],
			["unit_online_variable_type_list", "unit_online_variable_type_integer"],
			["unit_online_variable_type_list", "unit_online_variable_type_linear"],
			["unit_online_variable_type_list", "unit_online_variable_type_none"],
			["variable_type_list", "variable_type_binary"],
			["variable_type_list", "variable_type_continuous"],
			["variable_type_list", "variable_type_integer"],
			["write_mps_file_list", "write_mps_always"],
			["write_mps_file_list", "write_mps_never"],
			["write_mps_file_list", "write_mps_on_no_solve"],
			["db_mip_solver_list", "KNITRO.jl"],
			["db_mip_solver_list", "Cbc.jl"],
			["db_mip_solver_list", "CPLEX.jl"],
			["db_mip_solver_list", "HiGHS.jl"],
			["db_mip_solver_list", "Xpress.jl"],
			["db_mip_solver_list", "GLPK.jl"],
			["db_mip_solver_list", "Gurobi.jl"],
			["db_mip_solver_list", "Juniper.jl"],
			["db_mip_solver_list", "MosekTools.jl"],
			["db_mip_solver_list", "SCIP.jl"],
			["db_lp_solver_list", "KNITRO.jl"],
			["db_lp_solver_list", "CDCS.jl"],
			["db_lp_solver_list", "CDDLib.jl"],
			["db_lp_solver_list", "Clp.jl"],
			["db_lp_solver_list", "COSMO.jl"],
			["db_lp_solver_list", "CPLEX.jl"],
			["db_lp_solver_list", "CSDP.jl"],
			["db_lp_solver_list", "ECOS.jl"],
			["db_lp_solver_list", "Xpress.jl"],
			["db_lp_solver_list", "GLPK.jl"],
			["db_lp_solver_list", "Gurobi.jl"],
			["db_lp_solver_list", "HiGHS.jl"],
			["db_lp_solver_list", "Hypatia.jl"],
			["db_lp_solver_list", "Ipopt.jl"],
			["db_lp_solver_list", "MadNLP.jl"],
			["db_lp_solver_list", "MosekTools.jl"],
			["db_lp_solver_list", "NLopt.jl"],
			["db_lp_solver_list", "OSQP.jl"],
			["db_lp_solver_list", "ProxSDP.jl"],
			["db_lp_solver_list", "SCIP.jl"],
			["db_lp_solver_list", "SCS.jl"],
			["db_lp_solver_list", "SDPA.jl"],
			["db_lp_solver_list", "SDPNAL.jl"],
			["db_lp_solver_list", "SDPT3.jl"],
			["db_lp_solver_list", "SeDuMi.jl"]
		],
		"relationships" : [],
		"object_parameter_values" : [],
		"relationship_parameter_values" : [],
	    "alternatives" : [["Base", "Base alternative"]]
	}
    return spineopttemplate

def spineopt_basic_model():
    spineoptbasicmodel = {   
		"objects": [
			["model", "simple", None],
			["report", "report1", None],
			["stochastic_scenario", "realization", None],
			["stochastic_structure", "deterministic", None],
			["temporal_block", "flat", None]
		],
		"relationships": [
			["model__default_stochastic_structure", ["simple", "deterministic"]],
			["model__default_temporal_block", ["simple", "flat"]],
			["model__report", ["simple", "report1"]],
			["stochastic_structure__stochastic_scenario", ["deterministic", "realization"]]
		],
		"object_parameter_values": [
			["temporal_block", "flat", "resolution", {"data": "1h", "type": "duration"}, "Base"]
		]   
	}
    return spineoptbasicmodel

def map_preprocess(iodb):
	# Load SpineOpt template
    print("Load SpineOpt template")

    spineopttemplate = spineopt_template()
    spineoptbasicmodel = spineopt_basic_model()
	
    iodb.update(spineopttemplate)
    iodb.update(spineoptbasicmodel)
	

	# The template functionality of SpineOpt should be updated with a model template and a system template,
	# for now that is done manually in the workflow
    return

def map_postprocess(iodb):
    return

# Function map for entity classes; specific to the generic structure
def map_constraint(iodb,entities,parameters):
    return

def map_link(iodb,entities,parameters):
    entityname = entities[0]
    iodb["objects"].append(["connection", entityname, None])
    return

def map_node(iodb,entities,parameters):
    entityname = entities[0]
    parameter = parameters[0]
    iodb["objects"].append(["node",entityname,None])
    balancetype = "balance_type_none"
    if parameter["node_type"] == "balance":
        balancetype = "balance_type_node"
    iodb["object_parameter_values"].append(["node", entityname, "balance_type", balancetype, "Base"])
    if parameter["flow_profile"] != None:
        iodb["object_parameter_values"].append(["node",entityname,"demand",parameter["flow_profile"],"Base"])
    return

def map_period(iodb,entities,parameters):
    return

def map_set(iodb,entities,parameters):
      return

def map_solve_pattern(iodb,entities,parameters):
    return

def map_system(iodb,entities,parameters):
    return

def map_temporality(iodb,entities,parameters):
    return

def map_tool(iodb,entities,parameters):
    return

def map_unit(iodb,entities,parameters):
    entityname = entities[0]
    iodb["objects"].append(["unit",entityname,None])
    return

def map_node__to_unit(iodb,entities,parameters):
    nodename = entities[1]
    unitname = entities[2]
    unitparameters = parameters[2]
    iodb["relationships"].append(["unit__from_node", [unitname, nodename]])

    try:# may be easier when using the parameter functions
        nodenameplus = iodb.pop("unit__node__node__"+unitname)
        threewayrelation = [unitname, nodenameplus, nodename]
        iodb["relationships"].append(["unit__node__node",threewayrelation])
        iodb["relationship_parameter_values"].append(["unit__node__node",threewayrelation,"fix_ratio_out_in_unit_flow",unitparameters["efficiency"],"Base"])
    except:
        iodb["unit__node__node__"+unitname] = nodename
    
    return

def map_set__link(iodb,entities,parameters):
    return

def map_set_node(iodb,entities,parameters):
    return

def map_set_temporality(iodb,entities,parameters):
    return

def map_set__unit(iodb,entities,parameters):
    return

def map_tool_set(iodb,entities,parameters):
    return

def map_unit__to_node(iodb,entities,parameters):
    unitname = entities[1]
    nodename = entities[2]
    unitnodeparameters = parameters[0]
    unitparameters = parameters[1]
    iodb["relationships"].append(["unit__to_node", [unitname, nodename]])

    iodb["relationship_parameter_values"].append(["unit__to_node",entities,"vom_cost",unitnodeparameters["other_operational_cost"],"Base"])
    iodb["relationship_parameter_values"].append(["unit__to_node",entities,"unit_capacity",unitnodeparameters["capacity"],"Base"])

    try:# may be easier when using the parameter functions
        nodenameplus = iodb.pop("unit__node__node__"+unitname)
        threewayrelation = [unitname, nodename, nodenameplus]
        iodb["relationships"].append(["unit__node__node",threewayrelation])
        iodb["relationship_parameter_values"].append(["unit__node__node",threewayrelation,"fix_ratio_out_in_unit_flow",unitparameters["efficiency"],"Base"])
    except:
        iodb["unit__node__node__"+unitname] = nodename
    
    return

def map_node__link__node(iodb,entities,parameters):
    nodename = entities[1]
    linkname = entities[2]
    nodenameplus = entities[3]
    linkparameters = parameters[2]

    threewayrelation = [linkname, nodename, nodenameplus]
    iodb["relationships"].append(["connection__node__node", threewayrelation])
    iodb["relationship_parameter_values"].append(["connection__node__node",threewayrelation,"connection_capacity",linkparameters["capacity"],"Base"])
    iodb["relationship_parameter_values"].append(["connection__node__node",threewayrelation,"fix_ratio_out_in_connection_flow",linkparameters["efficiency"],"Base"])

    return

def map_set__node__temporality(iodb,entities,parameters):
    return

def map_set__node__unit(iodb,entities,parameters):
    return